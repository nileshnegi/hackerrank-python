"""
Validating UID

The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:
It must contain at least `2` uppercase English alphabet characters.
It must contain at least `3` digits.
It should only contain alphanumeric characters `(a-z, A-Z and 0-9)`.
No character should repeat.
There must be exactly `10` characters in a valid UID.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        uid = input()
        checks = {
            "alpha" : lambda uid: re.match(r".*[A-Z].*[A-Z].*", uid),
            "num" : lambda uid: re.match(r".*[0-9].*[0-9].*[0-9].*", uid),
            "alpha_num" : lambda uid: re.match(r"[A-Za-z0-9]{10}", uid),
            "repeat" : lambda uid: not re.match(r".*(.).*\1.*", uid)
        }

        print("Valid" if all(checks[check](uid) for check in checks.keys()) else "Invalid")
