"""
Zeros and Ones

You are given the shape of the array in the form of space-seperated integers
and you should print an array of 0s and array of 1s in integer format.
"""
import numpy as np


if __name__ == '__main__':
    N = tuple(map(int, input().rsplit()))

    print(np.zeros(N, dtype = np.int))
    print(np.ones(N, dtype = np.int))