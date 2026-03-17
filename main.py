from github import getRepoCommits, getRepos
from general import getEnv

def main():
    ENV = getEnv() # Holds all environment variables 

    repos = getRepos(ENV)
    counter = 0
    with open("commits.txt", "a", encoding="utf-8") as file:
        for repo in repos:
            commits = getRepoCommits(ENV, repo)
            for commit in commits:
                commit_endl = commit + "\n"
                print(commit_endl)
                file.write(commit_endl)


    # getRepoCommits(ENV, "https://api.github.com/repos/AndrewRoddy/timestamp")


if __name__ == "__main__":
    main()
