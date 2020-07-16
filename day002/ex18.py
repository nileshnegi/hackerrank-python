"""
String Validators

You are given a string ```S```.
Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()

    results = [False, False, False, False, False]
    for char in s:
        if char.isalnum():
            results[0] = True
            if char.isnumeric():
                results[2] = True
            elif char.isalpha():
                results[1] = True
                if char.isupper():
                    results[4] = True
                else:
                    results[3] = True
        
    for result in results:
        print(result)