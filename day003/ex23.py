"""
Alphabet Rangoli

You are given an integer, ```N```. Your task is to print an alphabet rangoli of size ```N```. (Rangoli is a form of Indian folk art based on creation of patterns.)
The center of the rangoli has the first alphabet letter a, and the boundary has the alphabet letter (in alphabetical order).
"""
import string

def print_rangoli(size):
    for i in range(size):
        print("-"*2*(size - i - 1), end='')
        
        for j in range(i):
            print("{}-".format(string.ascii_lowercase[size-1-j]), end='')
        print(string.ascii_lowercase[size-1-i], end='')
        for j in range(i):
            print("-{}".format(string.ascii_lowercase[size-i+j]), end='')
        
        print("-"*2*(size - i - 1))
    
    for i in range(size-2, -1, -1):
        print("-"*2*(size - i - 1), end='')
        
        for j in range(i):
            print("{}-".format(string.ascii_lowercase[size-1-j]), end='')
        print(string.ascii_lowercase[size-1-i], end='')
        for j in range(i):
            print("-{}".format(string.ascii_lowercase[size-i+j]), end='')
        
        print("-"*2*(size - i - 1))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)