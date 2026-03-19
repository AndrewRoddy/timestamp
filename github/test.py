from . import utcToZone
from . import isContributor
from . import formatCommits
from general import getEnv

def test_utcToZone():
    # checks for empty time zone (should default to EST)
    assert utcToZone(date="2026-03-06T04:10:12Z") == "2026-03-05 23:10:12"
    assert utcToZone("America/New_York", "2026-03-06T04:10:12Z") == "2026-03-05 23:10:12"
    
    # checks for daylight savings time
    assert utcToZone("America/New_York", "2026-03-07T04:10:12Z") == "2026-03-06 23:10:12"
    assert utcToZone("America/New_York", "2026-03-08T04:10:12Z") == "2026-03-07 23:10:12"
    
    # it would switch here
    assert utcToZone("America/New_York", "2026-03-09T03:10:12Z") == "2026-03-08 23:10:12"
    assert utcToZone("America/New_York", "2026-03-10T03:10:12Z") == "2026-03-09 23:10:12"

def test_isContributor():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    
    # # Checks for Organizations repo for is contributor
    # # Looks for Monster0506 in hacksu-website
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/hacksu-website") == True

    # # Checks for Organizations repo for not contributor
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/hacksu-website") == False

    # # Stress Test : checks for contributor in Linux
    # # https://github.com/torvalds/linux
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/torvalds/linux") == True

    # # Stress Test : checks for not contributor in Linux
    # Should assume he is in it because it is too large to check
    assert isContributor(PAT, "AndrewRoddy", "https://api.github.com/repos/torvalds/linux") == True

    # Also checks for contributor in regular person's repo
    # Looks for Monster0506 in rift
    # https://github.com/Monster0506/rift
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/Monster0506/rift") == True

    # Checks for not contributor in regular person's repo
    assert isContributor(PAT, "jamesTheJamesManManMan", "https://api.github.com/repos/Monster0506/rift") == False
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/Monster0506/rift") == False
    
    # Tests out empty repository (This whould always have no contributors)
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/khe-sponsorship") == False
    assert isContributor(PAT, "AndrewRoddy", "https://api.github.com/repos/hacksu/khe-sponsorship") == False
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/khe-sponsorship") == False

def test_formatCommits():
    commits = [
        [["2026-02-28"], ["19:10:50"], ["Start of project"], ["timestamp"]],
        [["2026-02-28"], ["19:20:45"], ["Started using uv"], ["other repo"]],
        [["2026-03-01"], ["21:51:43"], ["Edited environment variable example"], ["timestamp"]],
        [["2026-03-01"], ["21:53:00"], ["Updated implementation plan"], ["timestamp"]],
        [["2026-03-01"], ["22:54:54"], ["Attempted pagination for comit search, 1000 limit makes this impossible :("], ["timestamp"]],
        [["2026-03-02"], ["12:06:20"], ["Closer to pulling commits properly"], ["timestamp"]],
        [["2026-03-05"], ["16:38:20"], ["Fixed pagination for commits"], ["timestamp"]],
        [["2026-03-05"], ["16:53:00"], ["Pulled commit date properly"], ["timestamp"]],
        [["2026-03-05"], ["16:58:28"], ["Added time zone but I don't think it does anything"], ["timestamp"]],
        [["2026-03-05"], ["17:48:24"], ["Fixed empty response"], ["timestamp"]],
        [["2026-03-05"], ["18:14:15"], ["Thinking about how to manually convert to time zone"], ["my repo"]],
        [["2026-03-05"], ["22:02:36"], ["Seperated into github folder and added pytest"], ["timestamp"]],
        [["2026-03-05"], ["22:17:57"], ["Moved environment variable getting to a general module"], ["timestamp"]],
        [["2026-03-05"], ["22:59:44"], ["Moved github functions to proper place"], ["timestamp"]],
        [["2026-03-06"], ["09:31:33"], ["Implemented proper time zone conversion"], ["the repo"]],
        [["2026-03-06"], ["09:31:51"], ["Merge branch 'utc-to-tz'"], ["timestamp"]]
    ]

    formatted = formatCommits(commits)

    assert formatted["2026-02-28"] == """19:10:50 (timestamp) Start of project
19:20:45 (other repo) Started using uv"""
    assert formatted["2026-02-28"] == "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"

    # "21:51:43 (timestamp) Edited environment variable example
    # "21:53:00 (timestamp) Updated implementation plan
    # "22:54:54 (timestamp) Attempted pagination for comit search, 1000 limit makes this impossible :(

    # "12:06:20 (timestamp) Closer to pulling commits properly

    # "16:38:20 (timestamp) Fixed pagination for commits
    # "16:53:00 (timestamp) Pulled commit date properly
    # "16:58:28 (timestamp) Added time zone but I don't think it does anything
    # "17:48:24 (timestamp) Fixed empty response"
    # "18:14:15 (my repo) Thinking about how to manually convert to time zone"
    # "22:02:36 (timestamp) Seperated into github folder and added pytest
    # "22:17:57 (timestamp) Moved environment variable getting to a general module
    # "22:59:44 (timestamp) Moved github functions to proper place

    # "09:31:33 (the repo) Implemented proper time zone conversion"
    # "09:31:51 (timestamp) Merge branch 'utc-to-tz



# commits = [
#     [["2026-02-28"], ["19:10:50"], ["Start of project"], ["timestamp"]]
#     [["2026-02-28"], ["19:20:45"], ["Started using uv"], ["timestamp"]]
#     [["2026-02-28"], ["19:24:42"], ["Hides environment variables"], ["timestamp"]]
#     [["2026-02-28"], ["21:18:53"], ["Created function that gets all of the environment variables"], ["timestamp"]]
#     [["2026-02-28"], ["21:24:00"], ["Updated to make uv work good"], ["timestamp"]]
#     [["2026-02-28"], ["21:24:04"], ["Made README"], ["timestamp"]]
#     [["2026-02-28"], ["21:34:48"], ["Made it read from the envirnment variables properly"], ["timestamp"]]
#     [["2026-02-28"], ["22:11:20"], ["Can pull all current commits"], ["timestamp"]]
#     [["2026-02-28"], ["23:07:02"], ["Gets all public and private repos"], ["timestamp"]]
#     [["2026-02-28"], ["23:21:49"], ["Gets all repo names"], ["timestamp"]]
#     [["2026-02-28"], ["23:41:06"], ["Get all repos"], ["timestamp"]]
#     [["2026-02-28"], ["23:59:56"], ["Can now pull all of the commits"], ["timestamp"]]
#     [["2026-03-01"], ["00:57:08"], ["Created possible structure for the future"], ["timestamp"]]
#     [["2026-03-01"], ["01:06:51"], ["Added notes created and notes modified"], ["timestamp"]]
#     [["2026-03-01"], ["11:02:18"], ["Created template file"], ["timestamp"]]
#     [["2026-03-01"], ["11:32:27"], ["Created example template"], ["timestamp"]]
#     [["2026-03-01"], ["11:32:51"], ["Added template to the git ignore"], ["timestamp"]]
#     [["2026-03-01"], ["11:33:49"], ["Added order to the README on how the code will operate"], ["timestamp"]]
#     [["2026-03-01"], ["11:35:23"], ["Added methods of getting the data"], ["timestamp"]]
#     [["2026-03-01"], ["11:42:40"], ["Added motivation to README"], ["timestamp"]]
#     [["2026-03-01"], ["11:46:07"], ["Added tagline"], ["timestamp"]]
#     [["2026-03-01"], ["12:03:49"], ["Updated implementation plan"], ["timestamp"]]
#     [["2026-03-01"], ["12:09:51"], ["Update README.md"], ["timestamp"]]
#     [["2026-03-01"], ["12:11:06"], ["Update README.md"], ["timestamp"]]
#     [["2026-03-01"], ["15:08:14"], ["Fix grammatical errors in README motivation section"], ["timestamp"]]
#     [["2026-03-01"], ["21:51:43"], ["Edited environment variable example"], ["timestamp"]]
#     [["2026-03-01"], ["21:53:00"], ["Updated implementation plan"], ["timestamp"]]
#     [["2026-03-01"], ["22:54:54"], ["Attempted pagination for comit search, 1000 limit makes this impossible :("], ["timestamp"]]
#     [["2026-03-02"], ["12:06:20"], ["Closer to pulling commits properly"], ["timestamp"]]
#     [["2026-03-05"], ["16:38:20"], ["Fixed pagination for commits"], ["timestamp"]]
#     [["2026-03-05"], ["16:53:00"], ["Pulled commit date properly"], ["timestamp"]]
#     [["2026-03-05"], ["16:58:28"], ["Added time zone but I don't think it does anything"], ["timestamp"]]
#     [["2026-03-05"], ["17:48:24"], ["Fixed empty response"], ["timestamp"]]
#     [["2026-03-05"], ["18:14:15"], ["Thinking about how to manually convert to time zone"], ["timestamp"]]
#     [["2026-03-05"], ["22:02:36"], ["Seperated into github folder and added pytest"], ["timestamp"]]
#     [["2026-03-05"], ["22:17:57"], ["Moved environment variable getting to a general module"], ["timestamp"]]
#     [["2026-03-05"], ["22:59:44"], ["Moved github functions to proper place"], ["timestamp"]]
#     [["2026-03-06"], ["09:31:33"], ["Implemented proper time zone conversion"], ["timestamp"]]
#     [["2026-03-06"], ["09:31:51"], ["Merge branch 'utc-to-tz'"], ["timestamp"]]
#     [["2026-03-06"], ["09:32:38"], ["Found I don't own code50 or have any real way to pull it"], ["timestamp"]]
#     [["2026-03-06"], ["09:33:28"], ["Proper EST Timestamp is actually America/New_York"], ["timestamp"]]
#     [["2026-03-06"], ["09:40:19"], ["Cuts off the commit message after 60 characters"], ["timestamp"]]
#     [["2026-03-06"], ["09:50:05"], ["Changed getCommits to return a list of commits"], ["timestamp"]]
#     [["2026-03-06"], ["09:50:32"], ["deleted from commits.txt"], ["timestamp"]]
#     [["2026-03-06"], ["10:06:13"], ["Checks for noreply github email"], ["timestamp"]]
#     [["2026-03-06"], ["10:06:33"], ["Merge branch 'check-for-noreply'"], ["timestamp"]]
#     [["2026-03-17"], ["10:01:39"], ["Writes all commits to file"], ["timestamp"]]
#     [["2026-03-17"], ["10:01:57"], ["Adds commits.txt to the gitignore"], ["timestamp"]]
#     [["2026-03-17"], ["10:24:38"], ["Located broken repositories"], ["timestamp"]]
#     [["2026-03-17"], ["16:41:22"], ["Properly gets all repo commits"], ["timestamp"]]
#     [["2026-03-17"], ["16:45:58"], ["Sets up the headers for the request outside of the loop"], ["timestamp"]]
#     [["2026-03-18"], ["08:41:29"], ["Properly checks if user is a contributor"], ["timestamp"]]
#     [["2026-03-18"], ["08:42:05"], ["Finalized contributor checking (Closes #30)"], ["timestamp"]]
#     [["2026-03-18"], ["08:42:15"], ["Merge branch 'check-contributor'"], ["timestamp"]]
#     [["2026-03-18"], ["11:42:56"], ["Fixed isContributors"], ["timestamp"]]
#     [["2026-03-18"], ["11:58:11"], ["Finished implementing pagination when scanning through repos (Closes #31)"], ["timestamp"]]
#     [["2026-03-18"], ["11:59:08"], ["Merge branch 'Repo-Pagination'"], ["timestamp"]]
#     [["2026-03-18"], ["12:00:04"], ["Fixed up some comments"], ["timestamp"]]
# ]