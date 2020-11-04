"""
Re.split()

You are given a string `s` consisting only of digits `0-9`, commas `,`, and dots `.`.
Your task is to use re.split() to split the string delimited by `,` and `.` symbols.
"""
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
