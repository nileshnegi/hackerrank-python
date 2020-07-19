"""
Sum and Prod

You are given a 2-D array with dimensions ```N x M```.
Your task is to perform sum over axis 0 and then find the product of that result.
"""
import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    A = numpy.array(arr)
    
    print(numpy.prod(numpy.sum(A, axis=0), axis=0)