from filepaths import getPath

def test_getPath_default():
    assert getPath(
        "2000-12-31",
        "C:/Notes",
        "Daily-Notes",
        "YYYY/MM-MMMM/YYYY-MM-DD-dddd"
    ) == "C:/Notes/Daily-Notes/2000/12-December/2000-12-31-Sunday.md"

def test_getPath_dayChange():
    assert getPath(
        "2001-01-01", 
        "C:/Notes", 
        "Daily-Notes", 
        "YYYY/MM-MMMM/YYYY-MM-DD-dddd"
    ) == "C:/Notes/Daily-Notes/2001/01-January/2001-01-01-Monday.md"

def test_getPath_formatChange():
    assert getPath(
        "2001-01-01", 
        "C:/Notes", 
        "Daily-Notes", 
        "YYYY/MM/DD"
    ) == "C:/Notes/Daily-Notes/2001/01/01.md"

def test_getPath_pathChange():
    assert getPath(
        "2001-01-01", 
        "C:/Path/PathPath", 
        "Daily-Notes", 
        "YYYY/MM/DD"
    ) == "C:/Path/PathPath/Daily-Notes/2001/01/01.md"

def test_getPath_folderChange():
    assert getPath(
        "2001-01-01", 
        "C:/Path/PathPath", 
        "DAILYNOTES", 
        "YYYY/MM/DD"
    ) == "C:/Path/PathPath/DAILYNOTES/2001/01/01.md"
