
from datetime import datetime, date, timedelta

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
