"""
Company Logo

Given a string ```s``` which is the company name in lowercase letters,
your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If occurrence count is the same, sort the characters in alphabetical order.
"""
if __name__ == '__main__':
    s = input()
    occur = dict()
    result = []

    for char in s:
        if occur.get(char) == None:
            occur[char] = 1
        else:
            occur[char] += 1
    
    occur = dict(sorted(occur.items(), key=lambda item:(-item[1], item[0])))
    count = 3
    
    for k, v in occur.items():
        print(k, v)
        count -= 1
        if count == 0:
            break