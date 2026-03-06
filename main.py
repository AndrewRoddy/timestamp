from github import getRepoCommits, getRepos
from general import getEnv

# 2023(1585) + 2024(550) + 2025(1076) + 2026(920) - 1557
# 2574 commits

def main():
    ENV = getEnv() # Holds all environment variables 

    # repos = getRepos(ENV)
    # for repo in repos:
    getRepoCommits(ENV, "https://api.github.com/repos/AndrewRoddy/timestamp")


if __name__ == "__main__":
    main()
