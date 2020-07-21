"""
collections.Counter()

Raghu is a shoe shop owner. His shop has ```X``` number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are ```N``` number of customers who are willing to pay ```x```
amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
"""
from collections import Counter

if __name__ == "__main__":
    X = int(input())
    shoe_list = Counter(map(int, input().split()))
    result = 0

    for _ in range(int(input())):
        size, price = map(int, input().split())
        if size in shoe_list.keys() and shoe_list[size] != 0:
            result += price
            shoe_list[size] -= 1
    
    print(result)