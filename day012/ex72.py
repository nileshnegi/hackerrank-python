"""
Maximize it!

You are given a function `f(X) = X^2` and `K` lists, where the `i^th` list
contains `N_i` elements. Pick one element from each list so that the value 
for `S = (f(X_1) + f(X_2) + ... + f(X_K)) % M` is maximized.
"""
from itertools import product
from itertools import starmap

def f(X):
    return X*X


def compute(*L):
    res = 0
    for i in L:
        res += f(i)
    
    return(res)


if __name__ == '__main__':
    K, M = map(int, input().rsplit())
    N = list()

    for _ in range(K):
        N.append(list(map(int, input().rsplit()))[1:])
    
    res = list(product(*N))

    print(max([i%M for i in starmap(compute, res)]))
