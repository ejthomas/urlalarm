# URL Alarm: Load a web page by URL at a specified time

import time
import datetime
import webbrowser
import argparse

def process_input(input_dict):
    """
    Create and return a datetime object corresponding to the user's
    requested time. Takes as input a dictionary of the command line arguments
    to the program.
    """
    # Date format UK:
    # DD/MM[/YYYY]
    # Date format US:
    # MM/DD[/YYYY]
    # Leading zeros not required and 2-digit years permitted
    # Time format 12 hour:
    # hh:mm[:ss][ ]<AM/PM>
    # AM/PM may be separated by a space or not, also may be upper/lower case
    # Time format 24 hour:
    # hh:mm[:ss]

def get_delay(target_datetime):
    """
    Find and return the duration between the current time and the user
    specified time. Can return a negative result.
    """
    current_time = datetime.now() # aware datetime object
    target_delta = target_datetime - current_time # timedelta object
    sleep_duration = target_delta.total_seconds()
    return sleep_duration


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", required=True, nargs="+")
    parser.add_argument("-d", "--date", required=False)
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-l", "--locale", required=False)
    parser.add_argument("-c", "--clock", required=False)
    args = parser.parse_args()

    target_datetime = process_input(args)

    delay = get_delay(target_datetime)

    time.sleep(delay) # Wait until time to "ring"

    webbrowser.open(args.url)

if __name__=="__main__":
    main()
