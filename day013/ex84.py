"""
Hex Color Code

You are given `N` lines of CSS code. Your task is to print all valid Hex
Color Codes, in order of their occurrence from top to bottom.
Specifications: A Hex color code starts with `#` and has 3 or 6 characters
from `0-9` or `A-F`/`a-f`.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        regex = re.compile(r'(?<!^)(#(?:[\dA-Fa-f]{3}){1,2})')
        for item in regex.findall(input()):
            print(item)
