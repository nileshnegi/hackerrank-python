"""
Lists

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
"""
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        line = input()
        cmd = line.split()[0]
        if cmd == "insert":
            lst.insert(int(line.split()[1]), int(line.split()[2]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(line.split()[1]))
        elif cmd == "append":
            lst.append(int(line.split()[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()