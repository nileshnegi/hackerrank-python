"""
Iterables and Iterators

Given a list of `N` lowercase english letters and an integer `K`,
select any `K` indices (assume 1-based indexing) with a uniform probability
from the list. Then compute probability that atleast one of these tuples
contains the letter 'a'
"""
from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    letters = input().rsplit()
    r = int(input())

    count = 0
    tuples = list(combinations(letters, r))

    for i in tuples:
        if 'a' in i:
            count += 1
    
    print(count/len(tuples))
