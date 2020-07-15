"""
Athlete Sort

You are given a spreadsheet that contains a list of ```N``` athletes and their details (such as age, height, weight and so on).
You are required to sort the data based on the ```K```th attribute and print the final resulting table.
"""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x:x[k])

    for athlete in arr:
        print(" ".join(list(map(str, athlete))))