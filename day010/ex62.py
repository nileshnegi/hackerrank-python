"""
Set .intersection() Operation

You are given two sets of student roll numbers. One set has subscribed
to the English newspaper, one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to 
both newspapers.
"""
if __name__ == "__main__":
    n = int(input())
    english = set(map(int, input().split()))
    b = int(input())
    french = set(map(int, input().split()))

    print(len(english.intersection(french)))