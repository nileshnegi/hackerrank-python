"""
**Triangle Quest 2

You are given a positive integer ```N```.
Your task is to print a palindromic triangle of size ```N```.
For example, a palindromic triangle of size ```5``` is:
1
121
12321
1234321
123454321

Restrictions: Using only one print statement inside a for loop from 1 to ```N```.
Cannot use:
  string operations
  for-loops
  unpacking (*)
"""
if __name__ == "__main__":
    for i in range(1, int(input())+1):
        #print(int('1'*i) ** 2)  # String literals not allowed
        print(((pow(10, i) - 1) // 9) ** 2)