"""
Eye and Identity

Your task is to print an array of size `NxM` with its main diagonal
elements as `1's` and other elements as `0's`.
"""
import numpy as np


if __name__ == '__main__':
     print(str(np.eye(*map(int, input().rsplit()))).replace('1',' 1').replace('0',' 0'))
