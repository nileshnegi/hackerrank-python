"""
Concatenate

Given two integer arrays of size `NXP` and `MXP`, your task is to
concatenate them along axis `0` in an array of size `(N+M)xP`.
"""
import numpy


if __name__ == '__main__':
    N, M, P = map(int, input().rsplit())
    
    arr1 = []
    for _ in range(N):
        arr1.append(input().rsplit())
    
    arr2 = []
    for _ in range(M):
        arr2.append(input().rsplit())
        
    print(numpy.concatenate((numpy.array(arr1).astype(int), numpy.array(arr2).astype(int)), axis=0))
