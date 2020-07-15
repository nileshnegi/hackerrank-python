"""
Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given ```n``` scores. Store them in a list and find the score of the runner-up. 
"""
def find_runner_up(arr):
    arr.sort()
    winner = arr[-1]
    for i in reversed(range(len(arr))):
        if arr[i] < winner:
            return arr[i]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(find_runner_up(list(arr)))