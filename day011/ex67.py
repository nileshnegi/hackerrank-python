"""
itertools.permutations()

Given a string `S`, print all possible permutations
of length `r` in a lexographic sorted order
"""
from itertools import permutations

if __name__ == '__main__':
    S, r = input().rsplit()
    r = int(r)

    for i in sorted(list(permutations(S, r))):
        print(''.join(i))
