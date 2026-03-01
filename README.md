# Timestamp
Create a log of everything you do online, every day. The data already exists, might as well use it.

### Motivation
Everyone has my data but me.
Google knows everything about me, GitHub knows every time I work, Spotify knows every song I have ever listened to, Apple Health knows every time my heart beats.
But you know who doesn't, me. If these companies are going to keep this data then I am going to use it to create something I enjoy. I want to be able to look back and see every day that I got a steam achievement and every day I commited code.

I think it will be so cool to see that the days I commited more code were the same days I got like no sleep lol. See what days I listened to a lot of music on and played a lot of video games on too.

### Installation
1. Rename the `.env.example` file to `.env`
2. Fill it out like a form
3. Then rename the `template.example.md` to `template.md`
4. You can remove things and edit the order, do not edit the text though
5. Then run the python file with `uv run` and it should just work

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
3. Begin scanning your obsidian for everything after the start date
    1. If missing a day create a blank file for that day
4. Get all dates from after the start date that don't have the 'key'
5. (For APIs) Based on the date adjust plan to not go over the limit
6. Pull all of data on the missing dates since the start date
7. Format the data
8. Append it to the end of the files that are missing it
    1. If there is no data still append the key
9. Repeat back at the template until everythihg is added

Methods of getting data
1. API Calls (GitHub, Microsoft ToDo)
2. Requesting data as a zip (YouTube, Spotify)
3. Exporting the data (Health, Calendar)

