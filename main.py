from github import getRepoCommits, getContributedRepos, getRepos, getAllCommits, formatCommits
from general import getEnv
from filepaths import getPath, dateRange
from datetime import datetime, date, timedelta


def main():
    ENV = getEnv() # Holds all environment variables 

    # commits = getAllCommits(
        #     ENV["GITHUB_PAT"],
        #     ENV["GITHUB_USERNAME"],
        #     ENV["GITHUB_EMAIL"],
        #     ENV["TIME_ZONE"]
        # )

        # commits = getRepoCommits(
        #     ENV["GITHUB_PAT"],
        #     ENV["GITHUB_USERNAME"],
        #     ENV["GITHUB_EMAIL"],
        #     ENV["TIME_ZONE"],
        #     "https://api.github.com/repos/AndrewRoddy/timestamp"
        # ) 
        
        # formatted = formatCommits(commits)

    # get today

    bday = ENV["BIRTHDAY"].split("/")
    start_date = date(int(bday[0]), int(bday[1]), int(bday[2]))
    end_date = date.today() - timedelta(1)
    for single_date in dateRange(start_date, end_date):
        day = str(single_date.strftime("%Y-%m-%d"))
        path = getPath(
            day, ENV["OBSIDIAN_PATH"],
            ENV["DAILY_NOTES_FOLDER"],ENV["CUSTOM_FORMAT"]
        )
        print(path)
        # if day in formatted:
        #     print(day)
        #     print(formatted[day], "\n")

    # "YYYY-MM-DD"
        


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