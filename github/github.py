import os
import requests
import json

def utcToZone(ENV, date):
    return date

def getRepos(ENV):
    repo_urls = set()

    # Getting stuff from GitHub
    GITHUB_PAT = ENV.get("GITHUB_PAT")
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

def getRepoCommits(ENV, repo_url):
    # I should have at least 4099 commits total
    GITHUB_PAT = ENV.get("GITHUB_PAT")
    headers = { 'Authorization': f'Bearer {GITHUB_PAT}' }  

    page = 1
    pages = []
    while (True):
        # Builds the URL and makes the request
        url = repo_url + f"/commits?per_page=100&page={page}"
        r = requests.get(url=url, headers=headers)
        
        # Checks the status code, if we are good, doesn't break
        if (r.status_code == 422 or r.status_code == 403 or not r.json()):
            break

        pages.append(r)
        page += 1

    # Switch back to using the repos and pulling all commits from each repo instead.
    with open("commits.txt", "a", encoding='utf-8') as file:
        for page in pages:
            for commit in page.json():

                # If it's not ur email, it not ur commit
                if ENV["GITHUB_EMAIL"] not in [
                    commit["commit"]["author"]["email"],
                    commit["commit"]["committer"]["email"]
                ]: continue

                date = commit["commit"]["author"]["date"]
                formatted_date = utcToZone(ENV, date)

                msg = commit["commit"]["message"]
                print(f"{formatted_date} {msg}")
