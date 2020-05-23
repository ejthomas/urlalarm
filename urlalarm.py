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
    date_split = input_dict.date.split("/")
    if input_dict.locale == "UK":
        # Date format UK:
        # DD/MM[/YYYY]
        day = int(date_split[0])
        month = int(date_split[1])
    elif input_dict.locale == "US":
        # Date format US:
        # MM/DD[/YYYY]
        month = int(date_split[0])
        day = int(date_split[1])
    else:
        print("An available locale was not provided. Run with flag '-h' for " +
              "a list of available locales.")
        # TODO: handle error case safely

    if len(date_split) > 2:
        year_str = date_split[2]
        if len(year_str) == 2:
            year = int("20"+year_str)
        else:
            year = int(year_str)
    else:
        year = datetime.now().year
    # Leading zeros not required and 2-digit years permitted

    if input_dict.clock == "12h"
        # Time format 12 hour:
        # hh:mm[:ss][ ]<AM/PM>
        # AM/PM may be separated by a space or not, also may be upper/lower case
        if len(input_dict.time) == 2:
            ampm_str = input_dict.time[1].lower()
            time_split = input_dict.time[0].split(":")
        else:
            ampm_str = input_dict.time[-2:]
            time_split = input_dict.time[:-2]
        if ampm_str == "am":
            hour = int(time_split[0])
        elif ampm_str == "pm":
            hour = (int(time_split[0]) + 12) % 24 # catches 12:00AM = 00:00
        minute = int(time_split[1])
        if len(time_split) > 2:
            second = time_split[2]
        else:
            second = 0
    elif input_dict.clock == "24h":
        # Time format 24 hour:
        # hh:mm[:ss]
        time_split = input_dict.time.split(":")
        hour = int(time_split[0])
        minute = int(time_split[1])
        if len(time_split) > 2:
            second = int(time_split[2])
        else:
            second = 0
    else:
        print("Clock must be set to '12h' or '24h' using '-c' or '--clock'.")
        # TODO: handle error safely

    targetS_datetime = datetime.datetime(year=year, month=month, day=day,
                                         hour=hour, minute=minute,
                                         second=second,
                                         tzinfo=datetime.now().tzinfo)
    return target_datetime

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
    parser.add_argument("-l", "--locale", required=True)
    parser.add_argument("-c", "--clock", required=False)
    args = parser.parse_args()

    target_datetime = process_input(args)

    delay = get_delay(target_datetime)
    if delay > 0:
        time.sleep(delay) # Wait until time to "ring"
    else:
        print("The requested time is in the past." +
              " Please specify a future time.")
        return

    webbrowser.open_new(args.url)

if __name__=="__main__":
    main()
