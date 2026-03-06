from github import *
from general import getEnv

# 2023(1585) + 2024(550) + 2025(1076) + 2026(920) - 1557
# 2574 commits

def main():
    ENV = getEnv() # Holds all environment variables 

    repos = getRepos(ENV)
    # for repo in repos:
    print(repos[1])
    getRepoCommits(ENV, repos[0])

if __name__ == "__main__":
    main()
