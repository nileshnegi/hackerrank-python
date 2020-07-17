"""
String Formatting

Given an integer, ```n```, print the following values for each integer ```i``` from 1 to n:
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above.
Each value should be space-padded to match the width of the binary value of ```n```.
"""
def print_formatted(number):
    bin_width = len(str(bin(number))) - 2

    for i in range(1, number+1):
        print("{0:{bin_width}d} {0:{bin_width}o} {0:{bin_width}X} {0:{bin_width}b}".format(i, bin_width=bin_width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)