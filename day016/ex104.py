"""
Shape and Reshape

You are given a space separated list of nine integers.
Your task is to convert this list into a `3X3` NumPy array.
"""
import numpy


if __name__ == '__main__':
    print(numpy.reshape(numpy.array(input().rsplit()).astype(int), (3,3)))
