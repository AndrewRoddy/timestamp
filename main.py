import os
import requests
import json

def getEnv():
    env = {}

    # Opens the file
    with open(".env", "r") as file:
        content = file.read()
        
        lines = content.split("\n") # Splits by line

        for line in lines:

            line = line.split("=") # Splits into key and value
            key = line[0]
            value = line[1]
            
            value = value[1:-1] # Removes quotes
            env[key] = value # Sets it in the dictionary

    return env

def main():
    env = getEnv() # Holds all environment variables 

    OBSIDIAN_PATH = env.get("OBSIDIAN_PATH")
    DAILY_NOTES_FOLDER = env.get("DAILY_NOTES_FOLDER")
    GITHUB_PAT = env.get("GITHUB_PAT")

    # DAILY_NOTES_PATH = OBSIDIAN_PATH + "/" + DAILY_NOTES_FOLDER

    # print(DAILY_NOTES_PATH)
    # print(os.chdir(DAILY_NOTES_PATH))
    # print(os.listdir('.'))

    # Getting stuff from GitHub
    url = 'https://api.github.com/graphql'
    json = { 'query' : """
    { viewer 
        { repositories(first: 30) 
            { totalCount pageInfo 
                { 
                    hasNextPage endCursor 
                } 
                edges {
                    node {
                        name 
                    } 
                } 
            } 
        } 
    }
    """ }
    api_token = GITHUB_PAT
    headers = {'Authorization': 'token %s' % api_token}

    r = requests.post(url=url, json=json, headers=headers)
    print (r.text)

if __name__ == "__main__":
    main() 