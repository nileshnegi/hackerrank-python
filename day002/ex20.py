"""
Text Wrap

You are given a string ```S``` and width ```w```.
Your task is to wrap the string into a paragraph of width ```w```.
"""
def wrap(string, max_width):
    return string if len(string) <= max_width else string[:max_width] + "\n" + wrap(string[max_width:], max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)