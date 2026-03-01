import os

def getEnv():
    env = {}
    with open(".env", "r") as file:
        content = file.read()
        content = content.split("=")
        # content[0] is OBSIDIAN_PATH
        # content[0].strip("\"") is "C:/Folder"
        env[content[0]]=content[1].strip("\"")

    return env

def main():
    env = getEnv() # Holds all environment variables 

    print(env.get("OBSIDIAN_PATH"))

    # print(os.chdir())
    # print(os.listdir('.'))


if __name__ == "__main__":
    main() 