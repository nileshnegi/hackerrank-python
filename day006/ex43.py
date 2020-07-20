"""
Set .symmetric_difference() Operation

You are given two sets of student roll numbers. One set has subscribed to 
the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to 
either the English or the French newspaper but not both.
"""
if __name__ == "__main__":
    num_students1 = int(input())
    students1 = set(map(int, input().split()))

    num_students2 = int(input())
    students2 = set(map(int, input().split()))

    print(len(students1.symmetric_difference(students2)))