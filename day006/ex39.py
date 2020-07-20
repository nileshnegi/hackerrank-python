"""
Dot and Cross

You are given two arrays ```A``` and ```B```. Both have dimensions of ```N x N```. Your task is to compute their matrix product ```AB```.
"""
import numpy

if __name__ == "__main__":
    N = int(input())

    arr1 = []
    arr2 = []

    for _ in range(N):
        arr1.append(list(map(int, input().split())))
    
    for _ in range(N):
        arr2.append(list(map(int, input().split())))

    A = numpy.array(arr1, int)
    B = numpy.array(arr2, int)

    print(numpy.matmul(A, B))