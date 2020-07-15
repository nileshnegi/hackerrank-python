"""
Input()

You are given a polynomial of a single indeterminate (or variable), ```x```.
You are also given the values of ```x``` and ```k```. Your task is to verify if ```P(x) == k```.
"""
if __name__ == "__main__":
    x, k = map(int, input().split())
    P = input()

    print(eval(P) == k)