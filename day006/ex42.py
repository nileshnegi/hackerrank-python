"""
Linear Algebra

You are given a square matrix ```A``` with dimensions ```N x N```. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.
"""
import numpy

if __name__ == "__main__":
    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(map(float, input().split())))

    A = numpy.array(arr, float)

    print(numpy.round(numpy.linalg.det(A), decimals=2))