"""
Re.findall() & Re.finditer()

You are given a string ```S```. It consists of alphanumeric characters,
spaces and symbols(+,-). Your task is to find all the substrings of that
contains or more vowels. Also, these substrings must lie in between consonants
and should contain vowels only.
"""
import re

if __name__ == "__main__":
    s = input()

    sub = re.findall(r'(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)
    if len(sub) == 0:
        print("-1")
    else:
        for i in sub:
            print(i)