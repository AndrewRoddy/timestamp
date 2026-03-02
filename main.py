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

    OBSIDIAN_PATH = env.get("OBSIDIAN_PATH")
    DAILY_NOTES_FOLDER = env.get("DAILY_NOTES_FOLDER")

    # DAILY_NOTES_PATH = OBSIDIAN_PATH + "/" + DAILY_NOTES_FOLDER

    # print(DAILY_NOTES_PATH)
    # print(os.chdir(DAILY_NOTES_PATH))
    # print(os.listdir('.'))

    # repo_urls = getRepos(env)
    
    # Prints them all out including the length


    # repo_url = repo_urls[0]

    # I should have at least 4099 commits total

    GITHUB_PAT = env.get("GITHUB_PAT")
    headers = {'Authorization': f'Bearer {GITHUB_PAT}'}

    # url = repo_url + "/commits?per_page=100"

    page = 1
    pages = []
    while (True):
        url = f"https://api.github.com/search/commits?q=author:AndrewRoddy&per_page=100&page={page}"
        r = requests.get(url=url, headers=headers)

        print(f"{r.status_code=}")
        if (r.status_code == 422 or r.status_code == 403):
            break

        pages.append(r)
        page += 1

    i = 0
    with open("data.txt", "a") as file:
        for page in pages:
            print(page.json())
            for commit in page.json()["items"]:
                file.write(f"{commit["commit"]["author"]["date"]} | {commit["commit"]["message"]}\n")
                i += 1
                print(i)
                

    # file.write(commit["commit"]["date"], commit["commit"]["message"])
                # file.write(commit["items"]["commit"]["author"]["date"], commit["commit"]["message"])
    # print(len(r.json()))

    # Check every day I need
    # Pull all of the days I need



if __name__ == "__main__":
    main() 