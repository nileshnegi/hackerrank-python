"""
Check Subset

You are given two sets ```A``` and ```B```.
Your job is to find if set ```A``` is a subset of set ```B```.

The first line will contain the number of test cases.
The first line of each test case contains the number of elements in ```A```.
The second line of each test case contains space separated elements of ```A```.
The third line of each test case contains the number of elements in ```B```.
The fourth line of each test case contains space separated elements of ```B```.
"""
if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        _, A = input(), set(map(int, input().split()))
        _, B = input(), set(map(int, input().split()))

        print(A.issubset(B))