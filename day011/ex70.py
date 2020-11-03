"""
Compress the String!

Given a string `S`, if a character `c` occurs consecutively `X` times in it,
replace these occurences with `(X, c)`
eg. Input: 122233211
Output: (1, 1) (3, 2) (2, 3) (1, 2) (2, 1)
"""
from itertools import groupby

if __name__ == '__main__':
    s = input()

    for k, v in groupby(s):
        print("({}, {})".format(len(list(v)), k), end=' ')
