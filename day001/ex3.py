"""
Nested Lists

Given the names and grades for each student in a class of ```N``` students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
"""
def find_second_lowest_scorers(students):
    students.sort(key=lambda student:student[1])
    
    studs = []
    lowest_score = students[0][1]
    second_lowest = lowest_score

    for student in students[1:]:
        if student[1] > lowest_score:
            second_lowest = student[1]
            break
    
    for student in students[1:]:
        if student[1] == second_lowest:
            studs.append(student[0])
    
    studs.sort()
    
    return studs

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    for student in find_second_lowest_scorers(students):
        print(student)