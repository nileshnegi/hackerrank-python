"""
Regex Substitution

You are given a text of `N` lines. Replace occurences of `&&` with `and`
and `||` with `or`.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))