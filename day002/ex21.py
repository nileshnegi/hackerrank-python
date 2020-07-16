"""
Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be ```N X M```. (```N``` is an odd natural number, and ```M``` is 3 times ```N```)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""
if __name__ == "__main__":
    N, M = map(int, input().split())

    for i in range(N//2):
        print(("-"*(3*((N//2) - i))) + (".|."*(2*i + 1)) + ("-"*(3*((N//2) - i))))
    
    print(("-"*((M-7)//2)) + "WELCOME" + ("-"*((M-7)//2)))

    for i in range(N//2):
        print(("-"*(3*(i + 1))) + (".|."*(2*((N//2) - i) - 1)) + ("-"*(3*(i + 1))))