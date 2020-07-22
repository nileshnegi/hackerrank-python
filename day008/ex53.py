"""
Collections.deque()

A deque is a double-ended queue. It can be used to add or remove elements
from both ends. Perform append, pop, popleft and appendleft methods on an
empty deque ```d```.
"""
from collections import deque

if __name__ == "__main__":
    d = deque()
    for _ in range(int(input())):
        cmd = input().split()
        if len(cmd) == 2:
            getattr(d, cmd[0])(int(cmd[1]))
        else:
            getattr(d, cmd[0])()
    
    print(*d)