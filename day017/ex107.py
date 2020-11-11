"""
Standardize Mobile Numbers using Decorators

You are given `N` mobile numbers. Sort them in ascending order, then print
them in the standard format: `+91 xxxxx xxxxx`. The given mobile numbers may
have `0`, `+91` or `91` written before the actual number. Alternatively,
there may not be any prefix at all.
"""
def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 {} {}".format(n[-10:-5], n[-5:]) for n in l)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
