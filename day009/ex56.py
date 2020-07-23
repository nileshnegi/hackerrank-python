"""
Introduction to Sets

Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average 
of all the ```N``` plants with distinct heights in her greenhouse.
"""
def average(array):
    array = set(array)
    return sum(array) / len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)