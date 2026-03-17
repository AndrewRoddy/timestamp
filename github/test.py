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
    
    # Checks for Organizations repo for is contributor
    # Looks for Monster0506 in hacksu-website
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/hacksu-website") == True

    # Checks for Organizations repo for not contributor
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/hacksu-website") == False

    # Stress Test : checks for contributor in Linux
    # https://github.com/torvalds/linux
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/torvalds/linux") == True

    # Stress Test : checks for not contributor in Linux
    assert isContributor(PAT, "AndrewRoddy", "https://api.github.com/repos/torvalds/linux") == False

    # Also checks for contributor in regular person's repo
    # Looks for Monster0506 in rift
    # https://github.com/Monster0506/rift
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/Monster0506/rift") == True

    # Checks for not contributor in regular person's repo
    assert isContributor(PAT, "jamesTheJamesManManMan", "https://api.github.com/repos/Monster0506/rift") == False
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/Monster0506/rift") == False