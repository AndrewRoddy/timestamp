from github import getRepoCommits, getRepos
from general import getEnv

def main():
    ENV = getEnv() # Holds all environment variables 

    

    # Broken
    # https://api.github.com/repos/HappyCoderHackathons/.github
    # https://api.github.com/repos/HappyCoderHackathons/geese
    # https://api.github.com/repos/HappyCoderHackathons/narr0w
    # https://api.github.com/repos/HappyCoderHackathons/prismo
    # https://api.github.com/repos/HappyCoderHackathons/spiral
    # https://api.github.com/repos/hacksu/godot-tutorial
    # https://api.github.com/repos/rbostap1/ISSO

    repos = getRepos(ENV["GITHUB_PAT"])
    
    # repos = ["https://api.github.com/repos/HappyCoderHackathons/prismo"]
    commits_list = []
    count = 0 
    for repo in repos:
        # if "t3chatclone" in repo:
        #     print("========NO======")

        # print(repo.split("/")[-1]) # Gets name after last slash
    
        commits = getRepoCommits(
            ENV["GITHUB_PAT"], ENV["GITHUB_EMAIL"], 
            ENV["GITHUB_USERNAME"], ENV["TIME_ZONE"], repo
            )
        commits_list.extend(commits)
        count += len(commits)

        # Prints info about the repos we are pulling
        DEBUG_PRINT = True
        if (DEBUG_PRINT == True):
            print(f"{count:04d} total;", end=" ")
            print(f"{len(commits):03d} commits;", end=" ")

            repo_name = repo.split("/")[-1] # Gets name after last slash
            print(repo_name)

    commits_sorted = sorted(commits_list)

    with open("commits.txt", "a", encoding="utf-8") as file:
        for commit in commits_sorted:
            commit_endl = commit + "\n"
            file.write(commit_endl)

if __name__ == "__main__":
    main()
