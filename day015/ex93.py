"""
Time Delta

Find the difference in seconds between two timestamps per testcase, in the
following format `Day DD Month YYYY hh:mm:ss +xxxx`, where `+xxxx` is the
time zone in UTC format.
"""
import os
from datetime import datetime


def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return int(abs(datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = str(time_delta(t1, t2))
        fptr.write(delta + '\n')

    fptr.close()
