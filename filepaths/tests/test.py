from filepaths import getPath

def test_getPath():
    o_path = "C:/Notes"
    dn_folder = "Daily-Notes"
    c_format = "YYYY/MM-MMMM/YYYY-MM-DD-dddd"

    day = "2000-12-31"
    assert getPath(day, o_path, dn_folder, c_format
    ) == "C:/Notes/Daily-Notes/2000/12-December/2000-12-31-Sunday.md"

    day = "2001-01-01"
    assert getPath(day, o_path, dn_folder, c_format
    ) == "C:/Notes/Daily-Notes/2001/01-January/2001-01-01-Monday.md"

    c_format = "YYYY/MM/DD"
    assert getPath(day, o_path, dn_folder, c_format
    ) == "C:/Notes/Daily-Notes/2001/01/01.md"

    o_path = "C:/Path/PathPath"
    assert getPath(day, o_path, dn_folder, c_format
    ) == "C:/Path/PathPath/Daily-Notes/2001/01/01.md"

    dn_folder = "DAILYNOTES"
    assert getPath(day, o_path, dn_folder, c_format
    ) == "C:/Path/PathPath/DAILYNOTES/2001/01/01.md"
