"""
**Validating Email Addresses with a Filter

You are given an integer ```N``` followed by ```N``` email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3
"""
import re

def fun(s):
    # return True if s is a valid email, else return False
    if s.find('@') == -1 or s.find('.') == -1:
        return False

    result = re.match(r"\b[\w-]+@[a-z0-9]+.[a-z]{1,3}\b", s)

    if result == None:
        return False
    elif result.group(0) == s:
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)