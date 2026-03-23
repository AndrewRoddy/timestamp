from github import isContributor
from general import getEnv


def test_isContributor_org_repos():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    # Checks for Organizations repo for is contributor
    # Looks for Monster0506 in hacksu-website
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/hacksu-website") == True

    # Checks for Organizations repo for not contributor
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/hacksu-website") == False

def test_isContributor_large_repo():
    # Stress Test : checks for contributor in Linux
    # https://github.com/torvalds/linux
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/torvalds/linux") == True

    # Stress Test : checks for not contributor in Linux
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
