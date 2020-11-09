"""
Map and Lambda Function

You have to generate a list of the first `N` fibonacci numbers, `0` being
the first number. Then, apply the map function and a lambda expression to
cube each fibonacci number and print the list.
"""
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    res = list()

    if n == 1:
        res.append(0)
    elif n == 2:
        res.append(0)
        res.append(1)
    elif n > 2:
        res.append(0)
        res.append(1)
        for i in range(2, n):
            res.append(res[i-1] + res[i-2])

    return res


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
