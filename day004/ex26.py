"""
Merge the Tools!

Consider a string ```s``` of length ```n```, where ```s = c0c1c2....cn-1``` and an integer ```k```, where ```k``` is a factor of ```n```.
Split ```s``` into ```n/k``` sub-segments where each subsegment ```t``` consists of a contiguous block of ```k``` characters in ```s```.
Then, use each ```t``` to create string ```u``` such that:
    The characters in ```u``` are a sub-sequence of the characters in ```t```
    Any repeat occurrence of a character is removed from the string such that each character in ```u``` occurs exactly once

Given ```s``` and ```k```, print ```n/k``` lines where each line ```i``` denotes string ```u```.
"""
def merge_the_tools(string, k):
    n = len(string)
    parts = n//k
    for i in range(parts):
        print("".join(dict.fromkeys(string[k*i:k*(i+1)])))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)