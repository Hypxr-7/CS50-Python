import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.match(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start_hour, start_min, start_am_pm, end_hour, end_min, end_am_pm = time.groups()

        # check for whether minutes were entered
        if start_min is None and end_min is None:
            start_min, end_min = 0, 0

        # converts to int
        start_hour, start_min, end_hour, end_min = map(int, [start_hour, start_min, end_hour, end_min])

        # coverts start time to 24-hour format
        if start_am_pm == "PM" and start_hour != 12:
            start_hour += 12
        elif start_am_pm == "AM" and start_hour == 12:
            start_hour = 0

        # converts end time to 24-hour format
        if end_am_pm == "PM" and end_hour != 12:
            end_hour += 12
        elif end_am_pm == "AM" and end_hour == 12:
            end_hour = 0

        # checks for time in range
        if not 0 <= start_hour <= 23 or not 0 <= start_min <= 59:
            raise ValueError
        if not 0 <= end_hour <= 23 or not 0 <= end_min <= 59:
            raise ValueError

        # return formatted string
        return (f"{start_hour:02d}:{start_min:02d} to {end_hour:02d}:{end_min:02d}")
    else:
        raise ValueError




if __name__ == "__main__":
    main()
