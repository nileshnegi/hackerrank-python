"""
itertools.product()

Given two lists `A` and `B`, compute their cartesian product `AxB`
Eg. `product(A, B)` returns the same as `((x,y) for x in A for y in B)`
"""
from itertools import product

if __name__ == '__main__':
    A = list(map(int, input().rsplit()))
    B = list(map(int, input().rsplit()))

    for i in product(A, B):
        print(i, end=' ')
