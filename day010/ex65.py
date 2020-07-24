"""
Re.start() & Re.end()

You are given a string ```S```. Your task is to find the
indices of the start and end of string ```k``` in ```S```.
"""
import re

if __name__ == "__main__":
    S = input()
    k = input()

    matches = re.finditer(rf'(?=({re.escape(k)}))', S)
    worked = 0

    for match in matches:
        worked = 1
        print("({}, {})".format(match.start(), match.start() + len(k) - 1))

    if worked == 0:
        print("(-1, -1)")