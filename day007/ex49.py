"""
DefaultDict Tutorial

In this challenge, you will be given 2 integers, ```n``` and ```m```.
There are ```n``` words, which might repeat, in word group ```A```.
There are ```m``` words belonging to word group ```B```.
For each ```m``` words, check whether the word has appeared in group ```A```.
Print the indices of each occurrence of ```m``` in group ```A```.
If it does not appear, print -1.
"""
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    d = defaultdict(list)

    for _ in range(n):
        d['A'].append(input())
    
    for _ in range(m):
        char = input()
        B = []
        for i, ch in enumerate(d['A']):
            if ch == char:
                B.append(i + 1)
        
        if B == []:
            print(-1)
        else:
            print(*B)