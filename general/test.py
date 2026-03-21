from . import getEnv

def test_getEnv():
    ENV = getEnv("general/testEnv.env")
    # Required ################
    assert ENV["OBSIDIAN_PATH"]=="C:/VaultName"
    assert ENV["DAILY_NOTES_FOLDER"]=="FolderName"
    # Copy from Daily Notes as "Custom format"
    assert ENV["CUSTOM_FORMAT"]=="YYYY/MM-MMMM/YYYY-MM-DD-dddd"
    # Named "Template file Location"
    assert ENV["DAILY_NOTE_TEMPLATE"]=="FolderName/Template"
    # Needs to follow the IANA time zone identifier
    assert ENV["TIME_ZONE"]=="America/New_York"
    assert ENV["BIRTHDAY"]=="YYYY-MM-DD"
    ###########################

    ##### 👾 GitHub Commits
    assert ENV["GITHUB_USERNAME"]=="MyUsername"
    assert ENV["GITHUB_EMAIL"]=="email@email.com"
    # Make sure it is under 365 days expiring
    #     if you are a part of any organizations
    assert ENV["GITHUB_PAT"]=="ubrpiguberipgbweriughuqyfpowqiurwqiopuofhaskjfbvfm"
    assert "GITHUB_START_DATE"  not in ENV
    assert "GITHUB_LAST_UPDATE" not in ENV
    ###########################

    ##### 🎮 Steam Achievements
    assert ENV["STEAM_API_KEY"]=="hjaklhfjasdhlfkjadhjkflfa"
    assert ENV["STEAM_ID"]=="123640923245236"
    ###########################
