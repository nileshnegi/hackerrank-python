"""
Validating Roman Numerals

You are given a string, and you have to validate whether it's a valid Roman numeral.
"""
thousand = "(?:(M){0,3})?"
hundred  = "(?:(D?(C){0,3})|(CM)|(CD))?"
ten      = "(?:(L?(X){0,3})|(XC)|(XL))?"
unit     = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousand + hundred + ten + unit + "$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))