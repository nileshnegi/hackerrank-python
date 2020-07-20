"""
Polynomials

You are given the coefficients of a polynomial ```P``` and another line containing ```x```. Your task is to find the value of ```P(x)```.
"""
import numpy

if __name__ == "__main__":
    P = list(map(float, input().split()))
    x = float(input())

    print(numpy.polyval(P, x))