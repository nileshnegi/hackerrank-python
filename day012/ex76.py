"""
Find angle MBC

Given sides AB and BC of a right angle traingle ABC, right angled at B,
find angle MBC where M is the midpoint of the hypotenuse AC.
"""
# -*- coding: utf-8 -*-
import math


if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    print("{}\u00b0".format(round(math.degrees(math.atan(AB/BC)))))
