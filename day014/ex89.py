"""
Validating Credit Card Numbers

A valid credit card has the following characteristics:
It must start with `4`, `5` or `6`.
It must contain exactly 16 digits `[0-9]`.
It may have digits in groups of 4, seperated by a hyphen `-`.
It must not use any seperators like ` `, `_`, etc.
It must not have `4` or more consecutive repeated digits.
"""
import re


if __name__ == '__main__':
    regex = re.compile(
        r"^"
        r"(?!.*(\d)(-?\1){3})"
        r"[456]"
        r"\d{3}"
        r"(?:-?\d{4}){3}"
        r"$"
    )
    for _ in range(int(input().strip())):
        print("Valid" if regex.search(input().strip()) else "Invalid")
