"""
sWAP cASE

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
def swap_case(s):
    return "".join([char.lower() if char.isupper() else char.upper() for char in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)