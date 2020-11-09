"""
Incorrect Regex

Find out if the input string `S` is a valid regex or not.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            re.compile(input())
        except:
            print(False)
        else:
            print(True)
