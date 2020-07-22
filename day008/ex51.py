"""
Collections.OrderedDict()

You are the manager of a supermarket. You have a list of items together
with their prices that consumers bought on a particular day. Your task
is to print each item_name and net_price in order of its first occurrence.
"""
from collections import OrderedDict

if __name__ == "__main__":
    cart = OrderedDict()

    for _ in range(int(input())):
        item = input().split()
        item_name = " ".join(item[:-1])
        if cart.get(item_name) == None:
            cart[item_name] = int(item[-1])
        else:
            cart[item_name] += int(item[-1])
    
    for k,v in cart.items():
        print(k, v)