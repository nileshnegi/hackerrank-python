# Problem statements from HackerRank Python practice

The topic of these bullet items reflect the title of each problem from HackerRank. What follows is a summary of the problem description.

1. List Comprehensions  
You are given three integers ```x```, ```y``` and ```z``` and representing the dimensions of a cuboid along with an integer ```n```.
Print a list of all possible coordinates given by ```(i, j, k)``` on a 3D grid where the sum of ```i + j + k``` is not equal to ```n```.

2. Find the Runner-Up Score!  
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given ```n``` scores. Store them in a list and find the score of the runner-up.

3. Nested Lists  
Given the names and grades for each student in a class of ```N``` students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

4. Finding the percentage  
Input a dictionary of student names and list of marks.
Output the average of these marks obtained by a particular student correct to 2 decimal places.

5. Lists  
Consider a list. You can perform the following functions:
insert i e: Insert integer ```e``` at position ```i```
print: Print the list
remove e: Delete the first occurrence of integer ```e```
append e: Insert integer ```e``` at the end of the list
sort: Sort the list
pop: Pop the last element from the list
reverse: Reverse the list
Initialize your list and read in the value of ```n``` followed by lines of ```n``` commands where each command will be of the types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

6. Tuples  
Given an integer ```n``` and ```n``` space-separated integers as input, create a tuple ```t``` of those integers. Then compute and print the result of ```hash(t)```

7. Zipped!  
The National University conducts an examination of ```N``` students in ```X``` subjects.
Your task is to compute the average scores of each student.

8. Input()  
You are given a polynomial of a single indeterminate (or variable), ```x```.
You are also given the values of ```x``` and ```k```. Your task is to verify if ```P(x) == k```.

9. Python Evaluation  
You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).

10. Athlete Sort  
You are given a spreadsheet that contains a list of ```N``` athletes and their details (such as age, height, weight and so on).
You are required to sort the data based on the ```K```th attribute and print the final resulting table.

11. Any or All  
Input a list of ```N``` integers. Check if they are all positive palindromic integers.

12. ginortS  
Input a string and sort it in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

13. sWAP cASE
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

14. String Split and Join
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

15. What's Your Name?
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following: "Hello _first name_ _last name_! You just delved into python."

16. Mutations
Read a given string, change the character at a given index and then print the modified string.

17. Find a String
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

18. String Validators
You are given a string ```S```.
Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

19. Text Alignment
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

    ```python
    #Replace all ______ with rjust, ljust or center.

    thickness = int(input()) #This must be an odd number
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).______(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))
    ```

20. Text Wrap
You are given a string ```S``` and width ```w```.
Your task is to wrap the string into a paragraph of width ```w```.

21. Designer Doormat
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
Mat size must be ```N X M```. (```N``` is an odd natural number, and ```M``` is 3 times ```N```)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
