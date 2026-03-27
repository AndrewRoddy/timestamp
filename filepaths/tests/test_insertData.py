from filepaths import insertData
from random import choice

# Just tests the regular likely implementation
def test_insertData_default():
    # The example correct answer
    pathA = "filepaths/tests/temp/01A_test_insertData.md"
    # The path without the data inserted
    pathB = "filepaths/tests/temp/01B_test_insertData.md"
    # The path we will be ineserting the data into
    pathT = "filepaths/tests/temp/test_insertData.md"

    # Copy over initial state into temp file
    with open(pathB, "r", encoding="utf-8") as fileB:
        with open(pathT, "w", encoding="utf-8") as fileT:
            fileT.truncate(0) # Clears the file out
            fileT.write(fileB.read()) # Copies initial state

    # What we will be inserting
    data = "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"
    header = "👾 GitHub Commits"

    # Checks for github inside
    insertData(pathT, header, data)

    with open(pathA, "r", encoding="utf-8") as fileA:
        with open(pathT, "r", encoding="utf-8") as fileT:
            fileA_text = fileA.read()
            fileT_text = fileT.read()
            print("---Correct---:\n", fileA.read())
            print("---My Insert---:\n", fileT.read())
            assert fileA.read() == fileT.read()

# Tests the extra space at the top
# Adds an extra space if it isn't there yet
def test_insertData_extra_space():
    # The example correct answer
    pathA = "filepaths/tests/temp/02A_test_insertData.md"
    # The path without the data inserted
    pathB = "filepaths/tests/temp/02B_test_insertData.md"
    # The path we will be ineserting the data into
    pathT = "filepaths/tests/temp/test_insertData.md"

    # Copy over initial state into temp file
    with open(pathB, "r", encoding="utf-8") as fileB:
        with open(pathT, "w", encoding="utf-8") as fileT:
            fileT.truncate(0) # Clears the file out
            fileT.write(fileB.read()) # Copies initial state

    # What we will be inserting
    data = "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"
    header = "👾 GitHub Commits"

    # Checks for github inside
    insertData(pathT, header, data)

    with open(pathA, "r", encoding="utf-8") as fileA:
        with open(pathT, "r", encoding="utf-8") as fileT:
            fileA_text = fileA.read()
            fileT_text = fileT.read()
            print("---Correct---:\n", fileA_text)
            print("---My Insert---:\n", fileT_text)
            assert fileA_text == fileT_text

# Checks for inserting at a different header level
# def test_insertData_header_level():
    # The example correct answer
    pathA = "filepaths/tests/temp/02A_test_insertData.md"
    # The path without the data inserted
    pathB = "filepaths/tests/temp/02B_test_insertData.md"
    # The path we will be ineserting the data into
    pathT = "filepaths/tests/temp/test_insertData.md"

    # Copy over initial state into temp file
    with open(pathB, "r", encoding="utf-8") as fileB:
        with open(pathT, "w", encoding="utf-8") as fileT:
            fileT.truncate(0) # Clears the file out
            fileT.write(fileB.read()) # Copies initial state

    # What we will be inserting
    data = "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"
    header = "👾 GitHub Commits"

    # Checks for github inside
    insertData(pathT, header, data)

    with open(pathA, "r", encoding="utf-8") as fileA:
        with open(pathT, "r", encoding="utf-8") as fileT:
            fileA_text = fileA.read()
            fileT_text = fileT.read()
            print("---Correct---:\n", fileA_text)
            print("---My Insert---:\n", fileT_text)
            assert fileA_text == fileT_text

# def test_hasHeader_no_header():
# def test_hasHeader_stress_test():