"""
Tuples

Given an integer ```n``` and ```n``` space-separated integers as input, create a tuple ```t``` of those integers. Then compute and print the result of ```hash(t)```
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    if len(list(integer_list)) == n:
        print(hash(tuple(integer_list)))
    else:
        print("n and number of space seperated integers do not match.")