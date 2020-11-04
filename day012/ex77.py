"""
Detect Floating Point Number

Given a string `N`, verify if it is a floating point number.
"""
import re

if __name__ == '__main__':
    for _ in range(int(input())):
        print(bool(re.match('^[+-]?[0-9]*\.[0-9]+$', input())))
