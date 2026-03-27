
from datetime import datetime, date, timedelta
from pathlib import Path

def getPath(DAY, OBSIDIAN_PATH, DAILY_NOTES_FOLDER, CUSTOM_FORMAT):

    date = datetime.strptime(DAY, "%Y-%m-%d")

    # Splits day up into its values
    year  = date.year
    month = date.month
    day   = date.day

    note_path = CUSTOM_FORMAT

    date_dict = {
        # Year
        "YYYY": "%Y",
        "YY":   "%y",
        # Month
        "MMMM": "%B",
        "MMM":  "%b",
        "MM":   "%m",
        # Day
        "dddd": "%A",
        "ddd":  "%a",
        # Day of Month
        "DD":   "%d",
    }

    for key, value in date_dict.items():
        note_path = note_path.replace(
            key,
            date.strftime(value)
        )

    path = OBSIDIAN_PATH + "/" + DAILY_NOTES_FOLDER + "/" + note_path + ".md"

    return path

def dateRange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

def checkForSource(SOURCE, PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
    
    return False

def makeTemplatedFile(new_path, OBSIDIAN_PATH, DAILY_NOTE_TEMPLATE):
    template_path = f"{OBSIDIAN_PATH}/{DAILY_NOTE_TEMPLATE}.md"
    new_path = Path(new_path)
    parent = new_path.parent

    DEBUG = False
    if DEBUG:
        print(new_path)
    
    parent.mkdir(parents=True, exist_ok=True)
    with new_path.open("a", encoding="utf-8") as file:
        with open(template_path, "r", encoding="utf-8") as template:
            file.write(template.read())

def hasHeader(path, header):
    with open(path, "r", encoding="utf=8") as file:
        if header in file.read():
            return True

    return False

def insertData(path, header, data, header_size=4):
    text = ""
    with open(path, "r", encoding="utf=8") as file:
        text = file.read()

    with open(path, "a", encoding="utf=8") as file:
        file.write("\n") # Starts on new line

        # Adds extra space to end of text if not present
        if text[-1] != "\n":
            file.write("\n")

        # Adds pound signs and header
        for i in range(header_size):
            file.write("#")
        file.write(" ")
        file.write(header)
        
        file.write("\n") # Newline after header
        file.write(data) # Adds in actual text
