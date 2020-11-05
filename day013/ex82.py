"""
Validating phone numbers

Given `N` inputs, check if they are a valid phone number.
A valid mobile number is a ten digit number starting with `7`, `8` or `9`.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if re.match(r'^[789]{1}\d{9}$', input()) else "NO")
