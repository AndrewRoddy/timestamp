import os
import requests
import json

def getEnv():
    DEBUG = False
    env = {}

    # Opens the file
    with open(".env", "r") as file:
        content = file.read()
        
        lines = content.split("\n") # Splits by line

        for line in lines:

            line = line.split("=") # Splits into key and value
            key = line[0]
            if (DEBUG): print("key :", key)
            if (len(line) == 1):
                env[key] = ""
                if (DEBUG): print("value : Skipped")
                break 
            
            value = line[1]
            if (DEBUG): print("value :", value, "\n")

            
            value = value[1:-1] # Removes quotes
            env[key] = value # Sets it in the dictionary

    return env

def getRepos(env):
    repo_urls = set()

    # Getting stuff from GitHub
    GITHUB_PAT = env.get("GITHUB_PAT")
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

    # Prints all repo names and counts
    # for temp_url in repo_urls: print(temp_url)
    # print(len(repo_urls))

    return repo_urls

def main():
    env = getEnv() # Holds all environment variables 

    # I should have at least 4099 commits total
    GITHUB_PAT = env.get("GITHUB_PAT")
    headers = {'Authorization': f'Bearer {GITHUB_PAT}'}
    # repo_url = getRepos(env)

    # print(f"{repo_url[0]=}")

    page = 1
    pages = []
    while (True):
        url = "https://api.github.com/repos/AndrewRoddy/timestamp" + "/commits?per_page=100&page=" + str(page)
        r = requests.get(url=url, headers=headers)
        # print(url)
        print(r.json())
        # print(type(r))
        print(f"{r.status_code=}")
        if (r.status_code == 422 or r.status_code == 403 or len(r) == 0):
            break

        pages.append(r)
        page += 1
        print(f"{page=}")

    # Switch back to using the repos and pulling all commits from each repo instead.
    i = 0
    with open("data.txt", "a") as file:
        for page in pages:
            print(page.json())
            # for commit in page.json()["items"]:
                # file.write(f"{commit["commit"]["author"]["date"]} | {commit["commit"]["message"]}\n")
                # i += 1
                # print(i)

if __name__ == "__main__":
    main() 