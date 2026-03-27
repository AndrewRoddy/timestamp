from filepaths import insertData
from random import choice

def test_insertData_default():
    # The example correct answer
    pathA = "filepaths/tests/temp/01A_test_insertData.md"
    # The path without the data inserted
    pathB = "filepaths/tests/temp/01B_test_insertData.md"
    # The path we will be ineserting the data into
    pathC = "filepaths/tests/temp/01C_test_insertData.md"

    # Copy over initial state into temp file
    with open(pathB, "r", encoding="utf-8") as fileB:
        with open(pathC, "w", encoding="utf-8") as fileC:
            fileC.truncate(0) # Clears the file out
            fileC.write(fileB.read()) # Copies initial state

    # What we will be inserting
    data = "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"
    header = "👾 GitHub Commits"

    # Checks for github inside
    insertData(pathC, header, data)

    with open(pathA, "r", encoding="utf-8") as fileA:
        with open(pathC, "r", encoding="utf-8") as fileC:
            print("---Correct---:\n", fileA.read())
            print("---My Insert---:\n", fileC.read())
            assert fileA.read() == fileC.read()
            

# def test_insertData_extra_space():
    # Should add a space below if one is not there
    # If one is there it should just insert. Basically make sure a space is above it
# def test_insertData_header_level():
# def test_insertData_noHeaders():
#     path = "filepaths/tests/temp/test1.md"
#     data = """##### 📝 Write - 🕰️ \n\n\n\n1.\n\n#### 👾 GitHub Commits"""
#     header = "👾 GitHub Commits"

#     with open(path, "w", encoding="utf-8") as fp:
#         fp.write(data)
#         fp.truncate(0)
    
#     # Checks for github inside
#     assert(hasHeader(path, header) == False)

# def test_hasHeader_stress_test():
#     path = "filepaths/tests/temp/test1.md"
#     data = ""

#     data = ""
#     for i in range(100_000):
#         data += choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}_+<>:\"/")

#     header = "👾 GitHub Commits"

#     with open(path, "w", encoding="utf-8") as fp:
#         fp.write(data)
    
#     # Checks for github inside
#     assert(hasHeader(path, header) == False)

#     with open(path, "w", encoding="utf-8") as fp:
#         fp.truncate(0)