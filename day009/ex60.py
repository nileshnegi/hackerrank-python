"""
Set .discard(), .remove() & .pop()

You have a non-empty set ```s``` and you have to execute ```N``` commands
given in ```N``` lines. The commands will be pop, remove and discard.
"""
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        cmd = input().split()
        if len(cmd) == 1:
            getattr(s, cmd[0])()
        else:
            getattr(s, cmd[0])(int(cmd[1]))
    
    print(sum(s))