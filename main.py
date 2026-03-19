from github import getRepoCommits, getContributedRepos, getRepos, getAllCommits, formatCommits
from general import getEnv
from datetime import date, timedelta

def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)



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
    
    formatted = formatCommits(commits)

    start_date = date(2013, 1, 1)
    end_date = date(2027, 6, 2)
    for single_date in daterange(start_date, end_date):
        day = str(single_date.strftime("%Y-%m-%d"))
        if day in formatted:
            print(day)
            print(formatted[day], "\n")


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