"""
Mean, Var and Std

You are given a 2-D array of size ```N x M```.
Your task is to find:
    The mean along ```axis 1```
    The var along ```axis 0```
    The std along ```axis None```
"""
import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    A = numpy.array(arr)

    print(numpy.mean(A, axis=1))
    print(numpy.var(A, axis=0))
    print(numpy.std(A, axis=None))