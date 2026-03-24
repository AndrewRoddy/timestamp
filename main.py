from github import getRepoCommits, getContributedRepos, getRepos, getAllCommits, formatCommits
from general import getEnv
from filepaths import getPath, dateRange, checkForSource, makeTemplatedFile, hasHeader
from datetime import datetime, date, timedelta
import os.path

def main():
    ENV = getEnv() # Holds all environment variables

    if ENV["CUSTOM_FORMAT"][-1] == "/":
        raise Exception("Custom format cannot be a directory.")

   


    # commits = getAllCommits(
    #     ENV["GITHUB_PAT"],
    #     ENV["GITHUB_USERNAME"],
    #     ENV["GITHUB_EMAIL"],
    #     ENV["TIME_ZONE"]
    # )
    
    # formatted = formatCommits(commits)

    # bday = ENV["BIRTHDAY"].split("-")
    # start_date = date(2026, 1, 1)
    # end_date = date.today() - timedelta(1)
    # for single_date in dateRange(start_date, end_date):
    

    single_date = date(2028, 1, 1)
    day = str(single_date.strftime("%Y-%m-%d"))
    path = getPath(
        day, ENV["OBSIDIAN_PATH"],
        ENV["DAILY_NOTES_FOLDER"],ENV["CUSTOM_FORMAT"]
    )

    if not os.path.isfile(path):
        makeTemplatedFile(
            path,
            ENV["OBSIDIAN_PATH"],
            ENV["DAILY_NOTE_TEMPLATE"]
        )

    if hasHeader(path, "👾 GitHub Commits"):
        print("Has Header")
    else:
        print("Does not have header")

    # SOURCE = "👾 GitHub Commits"
    # # Makes sure the file exists first

    
    # checkForSource(SOURCE, path)

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