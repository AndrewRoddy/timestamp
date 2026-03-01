import os

def getEnv():
    env = {}

    # Opens the file
    with open(".env", "r") as file:
        content = file.read()
        
        lines = content.split("\n") # Splits by line

        for line in lines:

            line = line.split("=") # Splits into key and value
            key = line[0]
            value = line[1]
            
            value = value[1:-1] # Removes quotes
            env[key] = value # Sets it in the dictionary

    return env

def main():
    env = getEnv() # Holds all environment variables 

    OBSIDIAN_PATH = env.get("OBSIDIAN_PATH")
    print(OBSIDIAN_PATH)
    # print(os.chdir(OBSIDIAN_PATH))
    # print(os.listdir('.'))


if __name__ == "__main__":
    main() 