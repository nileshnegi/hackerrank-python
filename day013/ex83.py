"""
Validating and Parsing Email Addresses

A valid email address meets the following criteria -- It's composed of a username,
domain name, and extension assembled in this format: `username@domain.extension`.
The username starts with an English alphabetical character, and any subsequent
characters consist of one or more of the following: alphanumeric characters, `-`, `.`
and `_`. The domain and extension contain only English alphabetical characters.
The extension is `1`, `2` or `3` characters in length.
Given `n` pairs of names and email addresses as input, print each name and email
address pair having a valid email address on a new line.
"""
import re


if __name__ == '__main__':
    for _ in range(int(input())):
        name, email = input().rsplit()
        
        if re.match(r'^<{1}[a-zA-Z]{1}[a-zA-Z0-9\._\-]*@[a-zA-Z]+\.{1}[a-zA-Z]{1,3}>{1}$', email):
            print("{} {}".format(name, email))
