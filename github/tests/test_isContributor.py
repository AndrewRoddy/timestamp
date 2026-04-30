from github import isContributor
from general import getEnv
import pytest

import http.client as httplib

def hasInternet(
    url="www.geeksforgeeks.org",
    timeout=3
    ):
    connection = httplib.HTTPConnection(url,timeout=timeout)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except Exception as exp:
        return False

internet = hasInternet()

@pytest.mark.skip(reason="Not current")
@pytest.mark.skipif(internet == False, reason="No Internet")
def test_isContributor_org_repos():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    # Checks for Organizations repo for is contributor
    # Looks for Monster0506 in hacksu-website
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/hacksu-website") == True

    # Checks for Organizations repo for not contributor
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/hacksu-website") == False
    
@pytest.mark.skip(reason="Not current")
@pytest.mark.skipif(internet == False, reason="No Internet")
def test_isContributor_large_repos():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    # Stress Test : checks for contributor in Linux
    # https://github.com/torvalds/linux
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/torvalds/linux") == True

    # Stress Test : checks for not contributor in Linux
    # Should assume he is in it because it is too large to check
    assert isContributor(PAT, "AndrewRoddy", "https://api.github.com/repos/torvalds/linux") == True

@pytest.mark.skip(reason="Not current")
@pytest.mark.skipif(internet == False, reason="No Internet")
def test_isContributor_regular_repos():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    # Also checks for contributor in regular person's repo
    # Looks for Monster0506 in rift
    # https://github.com/Monster0506/rift
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/Monster0506/rift") == True

    # Checks for not contributor in regular person's repo
    assert isContributor(PAT, "jamesTheJamesManManMan", "https://api.github.com/repos/Monster0506/rift") == False
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/Monster0506/rift") == False
    
@pytest.mark.skip(reason="Not current")
@pytest.mark.skipif(internet == False, reason="No Internet")
def test_isContributor_empty_repos():
    ENV = getEnv()
    PAT = ENV["GITHUB_PAT"]
    # Tests out empty repository (This whould always have no contributors)
    assert isContributor(PAT, "Monster0506", "https://api.github.com/repos/hacksu/khe-sponsorship") == False
    assert isContributor(PAT, "AndrewRoddy", "https://api.github.com/repos/hacksu/khe-sponsorship") == False
    assert isContributor(PAT, "torvalds", "https://api.github.com/repos/hacksu/khe-sponsorship") == False
