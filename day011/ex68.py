"""
itertools.combinations()

Given a string `S`, print all possible combinations
upto length `r` in a lexographic sorted order
"""
from itertools import combinations

if __name__ == '__main__':
    S, r = input().rsplit()
    r = int(r)

    for i in range(1, r + 1):
        for j in list(combinations(sorted(S), i)):
            print(''.join(j))
