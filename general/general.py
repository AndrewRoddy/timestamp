
def getEnv(PATH=".env"):
    DEBUG = False
    env = {}

    # Opens the file
    with open(PATH, "r", encoding="utf-8") as file:
        content = file.read()
        
        lines = content.split("\n") # Splits by line

        for line in lines:
            
            # Skips lines without an = sign
            if "=" not in line: continue

            line = line.split("=") # Splits into key and value
            
            key = line[0]
            if (len(line) == 1):
                env[key] = ""
                if (DEBUG): print("value : Skipped")
                continue 
            
            # Skips ones that say DO_NOT_EDIT
            if line[1] == "\"DO_NOT_EDIT\"":
                continue

            value = line[1]
            value = value[1:-1] # Removes quotes
            env[key] = value # Sets it in the dictionary
    
    if (DEBUG):
        for key, value in env.items():
            print(key, value)

    return env