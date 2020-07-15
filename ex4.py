"""
Finding the percentage

Input a dictionary of student names and list of marks.
Output the average of these marks obtained by a particular student correct to 2 decimal places.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total = 0
    for score in student_marks[query_name]:
        total += score

    print("{0:.2f}".format(total/3))