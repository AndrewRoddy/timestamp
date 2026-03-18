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

def getRepos(GITHUB_PAT, GITHUB_USERNAME):
    repo_urls = set()

    DEBUG_PRINT = False

    # Getting stuff from GitHub
    headers = { 
        'Authorization': f'Bearer {GITHUB_PAT}',
        'User-Agent' : 'request'
    }

    urls = [
        'https://api.github.com/users/AndrewRoddy/repos?type=all&per_page=100', # public repos
        'https://api.github.com/user/repos?type=all&per_page=100' # private repos
    ]
    
    # Does the request on both URLs
    for url in urls:

        page = 1
        while (True):
            # Sets page then iterates it
            url_page = url + f"&page={page}"
            page += 1

            r = requests.get(url=url_page, headers=headers)

            # Prints the status code to see if broken repo
            if DEBUG_PRINT:
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

            for repo in r.json():
                repo_name = repo["url"]
                # Skips over repos where the user is not a contributor
                if isContributor(GITHUB_PAT, GITHUB_USERNAME, repo_name):
                    repo_urls.add(repo_name)
                    if DEBUG_PRINT:
                        print("🟢", repo_name.split("/")[-2], repo_name.split("/")[-1])
                elif DEBUG_PRINT:
                    print("🔴", repo_name.split("/")[-2], repo_name.split("/")[-1])

    # Converts URL's to a list then sorts them
    repo_urls = list(repo_urls)
    repo_urls_sorted = sorted(repo_urls)

    return repo_urls_sorted

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

    s = requests.Session()
    s.headers = headers

    page = 1
    url = REPO_URL + f"/contributors?per_page=100&page={page}"

    req = requests.Request('GET', url)
    r = s.get(url)
    

    # This is a solution for not being able to get the contributor list
        # This should basically just not matter because if its in your list you are probably a contributor at that point as these large repos aren't usually in orgs so checking if you are a contributor matters less
    # TypeError -> There isn't an error in the repo so just skip this check
    # ConnectionError/JSONDecodeError -> For when repo is archived or something
    try:
        if "The history or contributor list is too large" in r.json()["message"]:
            print("Repo too large to check, assuming you are a contributor.")
            return True
    except (TypeError):
        pass
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        return False
    

    # Checks for our user in user list
    for user in r.json():
        if str(user["login"]) == GITHUB_USERNAME:
            if DEBUG_PRINT:
                print("True", REPO_URL)
            return True

    if DEBUG_PRINT:
        print("False", REPO_URL)
    
    return False

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
        if DEBUG_PRINT:
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