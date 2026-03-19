from . import utcToZone
from . import isContributor
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
        "2025-10-15 00:23:58 Fixed bug where time does not updated while tabbed out",
        "2025-10-15 00:59:01 User can show or hide circles by clicking",
        "2025-10-15 01:20:18 Sends notification when break time is up",
        "2025-10-15 11:50:25 Added a lot of new ideas in ToDo",
        "2025-10-16 13:28:57 Added more to ToDo and created settings button component",
        "2025-10-16 16:22:20 Made the UI slightly better",
        "2025-10-16 16:51:03 Added settings button that doesn't do anything yet",
        "2025-10-16 16:57:35 Attempts to fix image icons",
        "2025-10-17 09:35:35 Assembly Studying",
        "2025-10-17 10:30:47 Completed 1a",
        "2025-10-17 11:40:03 Added favicon to tab",
        "2025-10-17 11:44:05 Part 1b complete",
        "2025-10-18 00:23:37 Updated formatting in spaces",
        "2025-10-18 02:05:22 Updated program counters, yeah, we have plural"
    ]
    formatted = formatCommits(commits)
    assert formatted["2025-10-15"] == [
        [["00:23:58"], ["Fixed bug where time does not updated while tabbed out"]],
        [["00:59:01"], ["User can show or hide circles by clicking"]],
        [["01:20:18"], ["Sends notification when break time is up"]],
        [["11:50:25"], ["Added a lot of new ideas in ToDo"]],
        ]