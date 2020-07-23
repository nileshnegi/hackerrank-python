"""
Symmetric Difference

Given 2 sets of integers, ```M``` and ```N```, print their symmetric
difference in ascending order. The term symmetric difference indicates
those values that exist in either or but do not exist in both.
"""
if __name__ == "__main__":
    M = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    B = set(map(int, input().split()))

    for i in sorted(A.symmetric_difference(B)):
        print(i)