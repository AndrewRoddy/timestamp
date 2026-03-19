from github import getRepoCommits, getContributedRepos, getRepos, getAllCommits
from general import getEnv

def main():
    ENV = getEnv() # Holds all environment variables 

    # commits = getAllCommits(
    #     ENV["GITHUB_PAT"],
    #     ENV["GITHUB_USERNAME"],
    #     ENV["GITHUB_EMAIL"],
    #     ENV["TIME_ZONE"]
    # )

    commits = getRepoCommits(
        ENV["GITHUB_PAT"],
        ENV["GITHUB_USERNAME"],
        ENV["GITHUB_EMAIL"],
        ENV["TIME_ZONE"],
        "https://api.github.com/repos/AndrewRoddy/timestamp"
    ) 
    
    for commit in commits:
        print(f"[[\"{commit[0]}\"], [\"{commit[1]}\"], [\"{commit[2]}\"], [\"{commit[3]}\"]],")

    # repos = getRepos(ENV["GITHUB_PAT"], ENV["GITHUB_USERNAME"])
    # for repo in repos:
    #     print(repo)

    # for commit in commits:
    #     print(commit)

    # with open("commits.txt", "a", encoding="utf-8") as file:
    #     for commit in commits:
    #         commit_endl = commit + "\n"
    #         file.write(commit_endl)

if __name__ == "__main__":
    main()