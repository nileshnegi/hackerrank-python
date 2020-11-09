"""
Matrix Script

The first line contains space-separated integers `N`(rows) and `M`(columns).
The next `N` lines contain the row elements of the matrix script.
To decode the script, replace symbols or spaces between 2 alphanumeric
characters with a single space for better readability.
"""
import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ""
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', string))
