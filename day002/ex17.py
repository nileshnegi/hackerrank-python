"""
Find a string

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
"""
def count_substring(string, sub_string):
    return (1 + count_substring(string[string.find(sub_string) + 1:], sub_string)) if (string.find(sub_string) != -1) else 0

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)