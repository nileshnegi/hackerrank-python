"""
Collections.namedtuple()

Dr. John Wesley has a spreadsheet containing a list of student IDs, marks,
class and names. These columns can be in any order for different testcases.
Your task is to help Dr. Wesley calculate the average marks of the students.
"""
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    students = namedtuple('students', input().split())
    result = 0

    for _ in range(N):
        result += int(students(*(input().split())).MARKS)
    
    print(result / N)