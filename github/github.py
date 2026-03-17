import os
import requests
import json

from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

def utcToZone(zone="America/New_York", date="1111-11-11T11:11:11Z"):
    # Converts from iso to datetime
    dt = datetime.fromisoformat(date)

    # Converts to my zone
    zoned_iso = dt.astimezone(ZoneInfo(zone))

    # Converts to the year and hour format
    converted = zoned_iso.strftime("%Y-%m-%d %H:%M:%S")

    return converted

def getRepos(GITHUB_PAT):
    repo_urls = set()

    # Getting stuff from GitHub
    headers = {'Authorization': f'Bearer {GITHUB_PAT}'}

    urls = [
        # All Public Repositories
        'https://api.github.com/users/AndrewRoddy/repos?type=all&per_page=100',

        # All private repositories
        'https://api.github.com/user/repos?type=all&per_page=100'
    ]
    
    # Does the request on both URLs
    for url in urls:
        r = requests.get(url=url, headers=headers)
        for repo in r.json():
            repo_urls.add(repo["url"])

    # Converts URL's to a list then sorts them
    repo_urls = list(repo_urls)
    repo_urls = sorted(repo_urls)

    return repo_urls

def isContributor(
    GITHUB_PAT,
    GITHUB_USERNAME,
    REPO_URL
    ):
    DEBUG_PRINT = False
    headers = { 
        'Authorization': f'Bearer {GITHUB_PAT}',
        'User-Agent' : 'request'
    }  
    page = 0
    url = REPO_URL + f"/contributors?per_page=100&page={page}"

    return True

def getRepoCommits(
    GITHUB_PAT,
    GITHUB_EMAIL,
    GITHUB_USERNAME,
    TIME_ZONE,
    REPO_URL
    ):

    DEBUG_PRINT = False

    headers = { 
        'Authorization': f'Bearer {GITHUB_PAT}',
        'User-Agent' : 'request'
    }  
    s = requests.Session()  # Establishes the session
    s.headers = headers # Sets the headers

    page = 1
    pages = []
    while (True):
        # Builds the URL and makes the request
        url = REPO_URL + f"/commits?per_page=100&page={page}"
        
        # Does the request
        req = requests.Request('GET', url) # Sets get request
        r = s.get(url)  # Prepares request
        
        # Prints the status code to see if broken repo
        if DEBUG_PRINT and r.status_code != 200:
            print(f"Status Code {r.status_code}")
            if r.status_code == 403:
                print(f"{r.headers.get('X-RateLimit-Limit')=}")
                print(f"{r.headers.get('X-RateLimit-Remaining')=}")
                print(f"{r.headers.get('X-RateLimit-Reset')=}")
                print(f"{r.json().get('message')=}")
        
        # Checks the status code, if we are good, doesn't break
        if (
            r.status_code == 422 or
            r.status_code == 403 or
            r.status_code == 404 or
            not r.json()):
            break

        pages.append(r)
        page += 1

    # Switch back to using the repos and pulling all commits from each repo instead.
    commits = []
    for page in pages:
        for commit in page.json():
            # If it's not ur email, it not ur commit
            # Checks for your github name in #########+GITHUBNAME@users.noreply.github.com email
            if (
                GITHUB_EMAIL    not in commit["commit"]["author"]["email"] and
                GITHUB_EMAIL    not in commit["commit"]["committer"]["email"] and
                GITHUB_USERNAME not in commit["commit"]["author"]["email"] and
                GITHUB_USERNAME not in commit["commit"]["committer"]["email"]
                ):
                continue

            date = commit["commit"]["author"]["date"]
            formatted_date = utcToZone(TIME_ZONE, date)

            msg = commit["commit"]["message"]
            first_line = msg.split("\n")[0]
            
            if len(first_line) > 60:
                first_line = first_line[:60]
                first_line += "..."

            commits.append(f"{formatted_date} {first_line}")

    return commits