"""
Word Order

You are given words. Some words may repeat. Print the total number of 
unique words. Also for each word, output its number of occurrences.
The output order should correspond with the input order of
appearance of the word.
"""
from collections import OrderedDict

if __name__ == "__main__":
    words = OrderedDict()

    for _ in range(int(input())):
        string = input()
        if words.get(string) == None:
            words[string] = 1
        else:
            words[string] += 1
    
    print(len(words.keys()))
    for value in words.values():
        print(value, end=" ")