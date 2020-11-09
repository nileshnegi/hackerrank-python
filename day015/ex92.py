"""
Calendar Module

You are given a date. Your task is to find what the day is on that date.
The input is in `MM DD YYYY` format.
"""
import calendar


if __name__ == '__main__':
    weekdays = {
        0 : "MONDAY",
        1 : "TUESDAY",
        2 : "WEDNESDAY",
        3 : "THURSDAY",
        4 : "FRIDAY",
        5 : "SATURDAY",
        6 : "SUNDAY"
    }

    month, day, year = map(int, input().rsplit())
    print(weekdays[calendar.weekday(year, month, day)])
