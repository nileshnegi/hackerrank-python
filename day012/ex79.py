"""
Group(), Groups() & Groupdict()

You are given a string `S`. Your task is to find the first occurrence
of an alphanumeric character in `S` (read from left to right) that has
consecutive repetitions.
"""
import re


if __name__ == '__main__':
    m = re.search(r'([a-zA-Z0-9])\1+', input().rstrip())
    print(m.group(1) if m else -1)