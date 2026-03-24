from github import formatCommits

def test_formatCommits_default():
    commits = [
        ["2026-02-28", "19:10:50", "Start of project", "timestamp"],
        ["2026-02-28", "19:20:45", "Started using uv", "other repo"],
        ["2026-03-01", "21:51:43", "Edited environment variable example", "timestamp"],
        ["2026-03-01", "21:53:00", "Updated implementation plan", "timestamp"],
        ["2026-03-01", "22:54:54", "Attempted pagination for comit search, 1000 limit makes this impossible :(", "timestamp"],
        ["2026-03-02", "12:06:20", "Closer to pulling commits properly", "timestamp"],
        ["2026-03-05", "16:38:20", "Fixed pagination for commits", "timestamp"],
        ["2026-03-05", "16:53:00", "Pulled commit date properly", "timestamp"],
        ["2026-03-05", "16:58:28", "Added time zone but I don't think it does anything", "timestamp"],
        ["2026-03-05", "17:48:24", "Fixed empty response", "timestamp"],
        ["2026-03-05", "18:14:15", "Thinking about how to manually convert to time zone", "my repo"],
        ["2026-03-05", "22:02:36", "Seperated into github folder and added pytest", "timestamp"],
        ["2026-03-05", "22:17:57", "Moved environment variable getting to a general module", "timestamp"],
        ["2026-03-05", "22:59:44", "Moved github functions to proper place", "timestamp"],
        ["2026-03-06", "09:31:33", "Implemented proper time zone conversion", "the repo"],
        ["2026-03-06", "09:31:51", "Merge branch 'utc-to-tz'", "timestamp"],
        ["2026-03-19", "16:18:19", "This commit is a test to see what I can do here !@#$%^&*()_+<>?:\"{}|,./;'[]\\`~1234567890\\\" \"\" \"\\\"\"", "timestamp"],
        ["2026-03-19", "16:18:43", "Merge branch 'format-commits'", "timestamp"],
    ]
    formatted = formatCommits(commits)

    assert formatted["2026-02-28"] == """19:10:50 (timestamp) Start of project
19:20:45 (other repo) Started using uv"""

    assert formatted["2026-02-28"]== "19:10:50 (timestamp) Start of project\n19:20:45 (other repo) Started using uv"

    assert formatted["2026-03-01"] == "21:51:43 (timestamp) Edited environment variable example\n21:53:00 (timestamp) Updated implementation plan\n22:54:54 (timestamp) Attempted pagination for comit search, 1000 limit makes this impossible :("

    assert formatted["2026-03-02"] == "12:06:20 (timestamp) Closer to pulling commits properly"

    assert formatted["2026-03-05"] == "16:38:20 (timestamp) Fixed pagination for commits\n16:53:00 (timestamp) Pulled commit date properly\n16:58:28 (timestamp) Added time zone but I don't think it does anything\n17:48:24 (timestamp) Fixed empty response\n18:14:15 (my repo) Thinking about how to manually convert to time zone\n22:02:36 (timestamp) Seperated into github folder and added pytest\n22:17:57 (timestamp) Moved environment variable getting to a general module\n22:59:44 (timestamp) Moved github functions to proper place"

    assert formatted["2026-03-06"] == "09:31:33 (the repo) Implemented proper time zone conversion\n09:31:51 (timestamp) Merge branch 'utc-to-tz'"

def test_formatCommits_special_chars():
    commits = [
        ["2026-03-19", "16:18:19", "This commit is a test to see what I can do here !@#$%^&*()_+<>?:\"{}|,./;'[]\\`~1234567890\\\" \"\" \"\\\"\"", "timestamp"],
        ["2026-03-19", "16:18:43", "Merge branch 'format-commits'", "timestamp"],
    ]
    formatted = formatCommits(commits)

    assert formatted["2026-03-19"] == """16:18:19 (timestamp) This commit is a test to see what I can do here !@#$%^&*()_+<>?:\"{}|,./;'[]\\`~1234567890\\\" \"\" \"\\\"\"
16:18:43 (timestamp) Merge branch 'format-commits'"""