
def getEnv():
    DEBUG = False
    env = {}

    # Opens the file
    with open(".env", "r") as file:
        content = file.read()
        
        lines = content.split("\n") # Splits by line

        for line in lines:

            line = line.split("=") # Splits into key and value
            key = line[0]
            if (DEBUG): print("key :", key)
            if (len(line) == 1):
                env[key] = ""
                if (DEBUG): print("value : Skipped")
                break 
            
            value = line[1]
            if (DEBUG): print("value :", value, "\n")

            
            value = value[1:-1] # Removes quotes
            env[key] = value # Sets it in the dictionary

    return env