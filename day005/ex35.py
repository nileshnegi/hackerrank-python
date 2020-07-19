"""
Floor, Ceil and Rint

You are given a 1-D array ```A```. Your task is to print the floor, ceil and rint of all the elements of ```A```. 
"""
import numpy

numpy.set_printoptions(sign=' ')  # needed because the expected output has a different format

if __name__ == "__main__":
    A = numpy.array(input().split(), float)

    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))