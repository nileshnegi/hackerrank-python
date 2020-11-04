"""
Polar Coordinates

You are given a complex number `z`. Your task is to convert it into polar
coordinates and print the modulus `r` and phase `phi`
"""
import cmath

if __name__ == '__main__':
    print(*cmath.polar(complex(input())), sep='\n')