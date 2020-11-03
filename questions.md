# Problem statements from HackerRank Python practice

The topic of these bullet items reflect the title of each problem from HackerRank. What follows is a summary of the problem description. (Note: *Question titles highlighted in bold are of interest*)

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

22. String Formatting  
Given an integer, ```n```, print the following values for each integer ```i``` from 1 to n: Decimal, Octal, Hexadecimal (capitalized) and Binary.
The four values must be printed on a single line in the order specified above.
Each value should be space-padded to match the width of the binary value of ```n```

23. Alphabet Rangoli  
You are given an integer, ```N```. Your task is to print an alphabet rangoli of size ```N```. (Rangoli is a form of Indian folk art based on creation of patterns.)
The center of the rangoli has the first alphabet letter a, and the boundary has the alphabet letter (in alphabetical order).

24. Capitalize!  
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, ```alison heck``` should be capitalised correctly as ```Alison Heck```.
Also ```12abc``` when capitalized remains ```12abc```.

25. **The Minion Game**  
Both players are given the same string, ```S```. Both players have to make substrings using the letters of this string.
Stuart has to make words starting with consonants. Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

26. Merge the Tools!  
Consider a string ```s``` of length ```n```, where ```s = c0c1c2....cn-1``` and an integer ```k```, where ```k``` is a factor of ```n```.
Split ```s``` into ```n/k``` sub-segments where each subsegment ```t``` consists of a contiguous block of ```k``` characters in ```s```.
Then, use each ```t``` to create string ```u``` such that: The characters in ```u``` are a sub-sequence of the characters in ```t``` and Any repeat occurrence of a character is removed from the string such that each character in ```u``` occurs exactly once.
Given ```s``` and ```k```, print ```n/k``` lines where each line ```i``` denotes string ```u```.

27. **Triangle Quest 2**  
You are given a positive integer ```N```.
Your task is to print a palindromic triangle of size ```N```.
Restrictions: Using only one print statement inside a for loop from 1 to ```N```. Cannot use: string operations, for-loops or unpacking.
For example, a palindromic triangle of size ```5``` is:

    ```python
    1
    121
    12321
    1234321
    123454321
    ```

28. Mod Divmod  
Read in two integers ```a``` and ```b``` and print three lines: The first line is the integer division: ```a // b```. The second line is the result of the modulo operator: ```a % b```. The third line prints the divmod of ```a``` and ```b```.

29. Power - Mod Power  
You are given three integers: ```a```, ```b``` and ```m```. Print two lines: The first line should print the result of ```pow(a,b)```. The second line should print the result of ```pow(a,b,m)```.

30. Integeres Come In All Sizes  
Read four numbers ```a```, ```b```, ```c``` and ```d```, and print the result of a^b + c^d.

31. **Triangle Quest**  
You are given a positive integer ```N```. Print a numerical triangle of height ```N-1``` like the one below. Can you do it using only arithmetic operations, a single for loop and print statement?

    ```python
    1
    22
    333
    4444
    55555
    ......
    ```

32. **Validating Email Addresses with a Filter**  
You are given an integer ```N``` followed by ```N``` email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:

    - It must have the username@websitename.extension format type.
    - The username can only contain letters, digits, dashes and underscores.
    - The website name can only have letters and digits.
    - The maximum length of the extension is 3

33. Reduce Function  
First line contains ```n```, the number of rational numbers.
The ```ith``` of next ```n``` lines contain two integers each, the numerator ```N``` and denominator ```D``` of the ```ith``` rational number in the list.
Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

34. Array Mathematics  
You are given two integer arrays ```A``` and ```B``` of dimensions ```N x M```. Your task is to perform the following operations: Add (```A + B```), Subtract (```A - B```), Multiply (```A * B```), Integer Division (```A / B```), Mod (```A % B```) and Power (```A ** B```).

35. Floor, Ceil and Rint  
You are given a 1-D array ```A```. Your task is to print the floor, ceil and rint of all the elements of ```A```.

36. Sum and Prod  
You are given a 2-D array with dimensions ```N x M```. Your task is to perform sum over axis 0 and then find the product of that result.

37. Min and Max  
You are given a 2-D array with dimensions ```N x M```. Your task is to perform the min function over ```axis=1``` and then find the max of that.

38. Mean, Var and Std  
You are given a 2-D array of size ```N x M```. Your task is to find: The mean along ```axis 1```, The var along ```axis 0``` and The std along ```axis None```.

39. Dot and Cross  
You are given two arrays ```A``` and ```B```. Both have dimensions of ```N x N```. Your task is to compute their matrix product ```AB```.

40. Inner and Outer  
You are given two arrays: ```A``` and ```B```. Your task is to compute their inner and outer product.

41. Polynomials  
You are given the coefficients of a polynomial ```P``` and another line containing ```x```. Your task is to find the value of ```P(x)```.

42. Linear Algebra  
You are given a square matrix ```A``` with dimensions ```N x N```. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

43. Set .symmetric_difference() Operation  
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

44. Set Mutations  
You are given a set ```A``` and ```N``` number of other sets. These ```N``` number of sets have to perform some specific mutation operations on set ```A```.
Your task is to execute those operations and print the sum of elements from set ```A```.
The first line contains the number of elements in set ```A```. The second line contains the space separated list of elements in set ```A```. The third line contains integer ```N```, the number of other sets.
The next ```2*N``` lines are divided into ```N``` parts containing two lines:
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line contains space separated list of elements in the other set.

45. The Captain's Room  
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms. One fine day, a finite number of tourists come to stay at the hotel. The tourists consist of: A Captain and An unknown group of families consisting of ```K``` members per group.
The Captain has a separate room, and the rest were given one room per group. Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists which will appear ```K``` times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number. The total number of tourists or the total number of groups is not known. You only know the value of ```K``` and the room number list.

46. Check Subset  
You are given two sets ```A``` and ```B```. Your job is to find if set ```A``` is a subset of set ```B```.
The first line will contain the number of test cases. The first line of each test case contains the number of elements in ```A```. The second line of each test case contains space separated elements of ```A```. The third line of each test case contains the number of elements in ```B```. The fourth line of each test case contains space separated elements of ```B```.

47. Check Strict Superset  
You are given a set ```A``` and ```N``` other sets.Your job is to find whether set ```A``` is a strict superset of each of these ```N``` sets.
A strict superset has at least one element that does not exist in its subset.

48. collections.Counter()  
Raghu is a shoe shop owner. His shop has ```X``` number of shoes. He has a list containing the size of each shoe he has in his shop. There are ```N``` number of customers who are willing to pay ```x``` amount of money only if they get the shoe of their desired size. Your task is to compute how much money Raghu earned.

49. DefaultDict Tutorial  
In this challenge, you will be given 2 integers, ```n``` and ```m```. There are ```n``` words, which might repeat, in word group ```A```. There are ```m``` words belonging to word group ```B```. For each ```m``` words, check whether the word has appeared in group ```A```. Print the indices of each occurrence of ```m``` in group ```A```. If it does not appear, print -1.

50. Collections.namedtuple()  
Dr. John Wesley has a spreadsheet containing a list of student IDs, marks, class and names. These columns can be in any order for different testcases. Your task is to help Dr. Wesley calculate the average marks of the students.

51. Collections.OrderedDict()  
You are the manager of a supermarket. You have a list of items together with their prices that consumers bought on a particular day. Your task is to print each item_name and net_price in order of its first occurrence.

52. Word Order  
You are given words. Some words may repeat. Print the total number of unique words. Also for each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.

53. Collections.deque()  
A deque is a double-ended queue. It can be used to add or remove elements from both ends. Perform append, pop, popleft and appendleft methods on an empty deque ```d```.

54. Piling Up!  
The first line contains a single integer ```T```, the number of test cases. For each test case, there are 2 lines. The first line of each test case contains ```n```, the number of cubes. The second line contains ```n``` space separated integers, denoting the sideLengths of each cube in that order.

55. Company Logo  
Given a string ```s``` which is the company name in lowercase letters, your task is to find the top three most common characters in the string. Print the three most common characters along with their occurrence count. Sort in descending order of occurrence count. If occurrence count is the same, sort the characters in alphabetical order.

56. Introduction to Sets  
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the ```N``` plants with distinct heights in her greenhouse.

57. Symmetric Difference  
Given 2 sets of integers, ```M``` and ```N```, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or but do not exist in both.

58. No Idea!  
There is an array of ```n``` integers. There are also 2 disjoint sets, ```A``` and ```B```, each containing integers. You like all the integers in set ```A``` and dislike all the integers in set ```B```. Your initial happiness is ```0```. For each integer in the array, if ```i in A```, you add ```1``` to your happiness. If ```i in B```, you add ```-1``` to your
happiness. Otherwise your happiness does not change. Output your final happiness at the end.

59. Set .add()  
The first line contains an integer ```N```, the total number of country stamps. The next ```N``` lines contains the name of the country where the stamp is from.

60. Set .discard(), .remove() & .pop()  
You have a non-empty set ```s``` and you have to execute ```N``` commands given in ```N``` lines. The commands will be pop, remove and discard.

61. Set .union() Operations  
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

62. Set .intersection() Operation  
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

63. Set .difference() Operation  
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

64. Re.findall() & Re.finditer()  
You are given a string ```S```. It consists of alphanumeric characters, spaces and symbols(+,-). Your task is to find all the substrings of that contains or more vowels. Also, these substrings must lie in between consonants and should contain vowels only.

65. Re.start() & Re.end()  
You are given a string ```S```. Your task is to find the indices of the start and end of string ```k``` in ```S```.

66. itertools.product()
Given two lists `A` and `B`, compute their cartesian product `AxB`. Eg. `product(A, B)` returns the same as `((x,y) for x in A for y in B)`.

67. itertools.permutations()
Given a string `S`, print all possible permutations of length `r` in a lexographic sorted order.

68. itertools.combinations()
Given a string `S`, print all possible combinations upto length `r` in a lexographic sorted order.

69. itertools.combinations_with_replacement()
Given a string `S`, print all possible combinations allowing elements to repeated more than once, of length `r` in a lexographic sorted order.

70. Compress the String!
Given a string `S`, if a character `c` occurs consecutively `X` times in it, replace these occurences with `(X, c)`. Eg. Input: 122233211 --> Output: (1, 1) (3, 2) (2, 3) (1, 2) (2, 1).

71. Iterables and Iterators
Given a list of `N` lowercase english letters and an integer `K`, select any `K` indices (assume 1-based indexing) with a uniform probability from the list. Then compute probability that atleast one of these tuples contains the letter 'a'.
