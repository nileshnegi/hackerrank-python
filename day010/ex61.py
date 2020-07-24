"""
Set .union() Operations

You are given two sets of student roll numbers. One set has subscribed
to the English newspaper, and the other set is subscribed to the French
newspaper. The same student could be in both sets. Your task is to find
the total number of students who have subscribed to at least one newspaper.
"""
if __name__ == "__main__":
    n = int(input())
    english = set(map(int, input().split()))
    b = int(input())
    french = set(map(int, input().split()))

    print(len(english.union(french)))