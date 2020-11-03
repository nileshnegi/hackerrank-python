"""
itertools.combinations_with_replacement()

Given a string `S`, print all possible combinations allowing elements
to repeated more than once, of length `r` in a lexographic sorted order
"""
from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, r = input().rsplit()
    r = int(r)

    for i in list(combinations_with_replacement(sorted(S), r)):
            print(''.join(i))
