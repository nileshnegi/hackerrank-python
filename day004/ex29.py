"""
Power - Mod Power

You are given three integers: ```a```, ```b``` and ```m```. Print two lines:
The first line should print the result of ```pow(a,b)```. The second line should print the result of ```pow(a,b,m)```. 
"""
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())

    print(pow(a, b))
    print(pow(a, b, m))