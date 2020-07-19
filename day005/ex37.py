"""
Min and Max

You are given a 2-D array with dimensions ```N x M```. Your task is to perform the min function over ```axis=1``` and then find the max of that.
"""
import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    A = numpy.array(arr)

    print(numpy.max(numpy.min(A, axis=1), axis=0))