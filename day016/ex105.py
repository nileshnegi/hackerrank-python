"""
Transpose and Flatten

You are given a `NXM` integer array matrix with space separated elements.
Your task is to print the transpose and flatten results.
"""
import numpy


if __name__ == '__main__':
    N, M = map(int, input().rsplit())
    
    arr = list()
    for _ in range(N):
        arr.append(input().rsplit())
        
    array = numpy.array(arr).astype(int)
    
    print(numpy.transpose(array))
    print(array.flatten())
