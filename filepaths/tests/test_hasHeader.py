from filepaths import hasHeader
from random import choice

def test_hasHeader_inside():
    path = "filepaths/tests/temp/test_hasHeader.md"
    data = """##### 📝 Write - 🕰️ \n\n\n\n1.\n\n#### 👾 GitHub Commits"""
    header = "👾 GitHub Commits"

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(data)
    
    # Checks for github inside
    assert(hasHeader(path, header) == True)

    with open(path, "w", encoding="utf-8") as fp:
        fp.truncate(0)

def test_hasHeader_empty():
    path = "filepaths/tests/temp/test_hasHeader.md"
    data = """##### 📝 Write - 🕰️ \n\n\n\n1.\n\n#### 👾 GitHub Commits"""
    header = "👾 GitHub Commits"

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(data)
        fp.truncate(0)
    
    # Checks for github inside
    assert(hasHeader(path, header) == False)

def test_hasHeader_stress_test():
    path = "filepaths/tests/temp/test_hasHeader.md"
    data = ""

    data = ""
    for i in range(100_000):
        data += choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}_+<>:\"/")

    header = "👾 GitHub Commits"

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(data)
    
    # Checks for github inside
    assert(hasHeader(path, header) == False)

    with open(path, "w", encoding="utf-8") as fp:
        fp.truncate(0)