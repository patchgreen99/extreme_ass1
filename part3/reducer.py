#!/usr/bin/python

import sys

largest_token = 0
largest_line = 0

for line in sys.stdin:  # For ever line in the input from stdin
    line = line.strip()  # Remove trailing characters
    token_len, line_len = line.split("\t", 1)

    temp = int(line_len)
    if largest_line < temp:
        largest_line = temp

    temp = int(token_len)
    if largest_token < temp:
        largest_token = temp

print("{0}\t{1}".format(largest_token,largest_line))