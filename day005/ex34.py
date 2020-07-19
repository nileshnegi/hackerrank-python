"""
Array Mathematics

You are given two integer arrays ```A``` and ```B``` of dimensions ```N x M```.
Your task is to perform the following operations:
    Add (```A + B```)
    Subtract (```A - B```)
    Multiply (```A * B```)
    Integer Division (```A / B```)
    Mod (```A % B```)
    Power (```A ** B```)
"""
import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr1 = []
    arr2 = []

    for _ in range(N):
        arr1.append(list(map(int, input().split())))
    
    for _ in range(N):
        arr2.append(list(map(int, input().split())))
    
    A = numpy.array(arr1)
    B = numpy.array(arr2)

    print(numpy.add(A, B))
    print(numpy.subtract(A, B))
    print(numpy.multiply(A, B))
    print(A //B)
    print(numpy.mod(A, B))
    print(numpy.power(A, B))