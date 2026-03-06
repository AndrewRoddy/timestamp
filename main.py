from github import getRepoCommits, getRepos
from general import getEnv

# 2023(1585) + 2024(550) + 2025(1076) + 2026(920) - 1557
# 2574 commits
# 1579 Captured so far

def main():
    ENV = getEnv() # Holds all environment variables 

    repos = getRepos(ENV)
    counter = 0
    for repo in repos:
        commits = getRepoCommits(ENV, repo)
        for commit in commits:
            print(commit)
            counter += 1
            print(counter)


    # getRepoCommits(ENV, "https://api.github.com/repos/AndrewRoddy/timestamp")


if __name__ == "__main__":
    main()
