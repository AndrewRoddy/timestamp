# Timestamp

### Motivation

### Implementation Plan

Everything we track should be immutable. 
    Meaning once the day has passed there should be no way/reason to edit it.
    This is important as once we add it, we don't need to update it.
    I only want to append to the files and editing them can cause data loss

'key' : "##### 👾 GitHub Commits"
1. Checks through the template for the first thing to implement
2. Checks the start date of task (ex : First day commiting to github)
    1. If there is no start date, it will pull all data and find it
    2. Then it will put that as the start date
3. Begin scanning repository for everything after the start date
4. Get all dates from after the start date that don't have the 'key'
5. (For APIs) Based on the date adjust plan to not go over the limit
6. Pull all of data on the missing dates since the start date
7. Format the data
8. Append it to the end of the files that are missing it
9. Repeat back at the template until everythihg is added

### Possible Structure

