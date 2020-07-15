"""
Any or All

Input a list of ```N``` integers. Check if they are all positive palindromic integers.
"""
if __name__ == "__main__":
    N = int(input())
    arr = list(input().rstrip().split())

    if all(list(map(lambda x:int(x) > 0, arr))):
        print(any(list(map(lambda x:x[::-1] == x, arr))))
    else:
        print(False)