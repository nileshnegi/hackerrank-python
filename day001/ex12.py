"""
ginortS

Input a string and sort it in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
if __name__ == "__main__":
    S = input()
    lowercase = []
    uppercase = []
    num = []
    for char in S:
        if char.isupper():
            uppercase.append(char)
        elif char.islower():
            lowercase.append(char)
        else:
            num.append(char)
    
    lowercase.sort()
    uppercase.sort()
    odd = [x for x in list(map(int, num)) if x%2 == 1]
    odd.sort()
    even = [x for x in list(map(int, num)) if x%2 == 0]
    even.sort()

    result = "".join(lowercase)
    result += "".join(uppercase)
    result += "".join(list(map(str, odd)))
    result += "".join(list(map(str, even)))

    print(result)