from github import getRepoCommits, getContributedRepos, getRepos, getAllCommits
from general import getEnv

def main():
    ENV = getEnv() # Holds all environment variables 

    # Maybe figure out bubble tea
    repos = getContributedRepos(
        ENV["GITHUB_PAT"],
        ENV["GITHUB_USERNAME"],
    )
    
    # commits = getAllCommits(
    #     ENV["GITHUB_PAT"],
    #     ENV["GITHUB_USERNAME"],
    #     ENV["GITHUB_EMAIL"],
    #     ENV["TIME_ZONE"]
    # )

    # for commit in commits:
    #     print(commit)
    

    # with open("commits.txt", "a", encoding="utf-8") as file:
    #     for commit in commits_sorted:
    #         commit_endl = commit + "\n"
    #         file.write(commit_endl)

if __name__ == "__main__":
    main()