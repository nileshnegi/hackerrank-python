"""
Check Strict Superset

You are given a set ```A``` and ```N``` other sets.
Your job is to find whether set ```A``` is a strict superset
of each of these ```N``` sets.
A strict superset has at least one element that does not exist in its subset. 
"""
if __name__ == "__main__":
    A = set(map(int, input().split()))
    ans = True

    for _ in range(int(input())):
        N = set(map(int, input().split()))
        if not A > N:
            ans = False
            break
    
    print(ans)