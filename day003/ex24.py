"""
Capitalize!

You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, ```alison heck``` should be capitalised correctly as ```Alison Heck```.
Also ```12abc``` when capitalized remains ```12abc```. 
"""
import re

def solve(s):
    return re.sub(r"\w+",
                  lambda mo: mo.group().capitalize(),
                  s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()