"""
Classes: Dealing with Complex Numbers

You are given two complex numbers, and you have to print the result of their
addition, subtraction, multiplication, division and modulus operations by
overloading methods of the in-built `Complex` class.
The real and imaginary precision part should be correct up to two decimal places.
"""
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    
    def __mul__(self, no):
        return Complex(self.real*no.real - self.imaginary*no.imaginary, self.real*no.imaginary + self.imaginary*no.real)

    def mod(self):
        return Complex(math.pow(self.real**2 + self.imaginary**2, 0.5), 0)
    
    def __truediv__(self, no):
        return Complex((self.real*no.real + self.imaginary*no.imaginary)/(no.real**2 + no.imaginary**2), (self.imaginary*no.real - self.real*no.imaginary)/(no.real**2 + no.imaginary**2))

    def __str__(self):
        if self.imaginary == 0:
            return "{0:.2f}+0.00i".format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                return "0.00+{0:.2f}i".format(self.imaginary)
            else:
                return "0.00-{0:.2f}i".format(abs(self.imaginary))
        elif self.imaginary > 0:
            return "{0:.2f}+{1:.2f}i".format(self.real, self.imaginary)
        else:
            return "{0:.2f}-{1:.2f}i".format(self.real, abs(self.imaginary))


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
