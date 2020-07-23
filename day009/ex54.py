"""
Piling Up!

The first line contains a single integer ```T```, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains ```n```, the number of cubes.
The second line contains ```n``` space separated integers, denoting the
sideLengths of each cube in that order. 
"""
from collections import deque

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        d = deque(map(int, input().split()))
        stack = []

        if d[0] <= d[-1]:
            stack.append(d.pop())
        else:
            stack.append(d.popleft())

        for i in range(1, N):
            if d[0] >= d[-1]:
                if d[0] > stack[-1]:
                    print("No")
                    break
                else:
                    stack.append(d.popleft())
            else:
                if d[-1] > stack[-1]:
                    print("No")
                    break
                else:
                    stack.append(d.pop())
        else:
            print("Yes")