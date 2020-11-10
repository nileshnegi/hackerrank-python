"""
Exceptions

Given two values `a` and `b`, perform integer division and print `a/b`.
In the case of `ZeroDivisionError` or `ValueError`, print the error code.
"""
if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = input().rsplit()
        try:
            a = int(a)
        except ValueError as e:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(a))
        else:
            try:
                b = int(b)
            except ValueError as e:
                print("Error Code: invalid literal for int() with base 10: '{}'".format(b))
            else:
                try:
                    print(a//b)
                except ZeroDivisionError as ze:
                    print("Error Code: integer division or modulo by zero")
