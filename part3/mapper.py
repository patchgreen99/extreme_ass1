#!/usr/bin/python

import sys

largest_token = 0
largest_line = 0

for line in sys.stdin:  # input from standard input
    temp = len(line.strip())
    if largest_line < temp:
        largest_line = temp

    tokens = line.split()  # split the line into tokens

    for token in tokens:  # write the results to standard input
        temp = len(token.strip())
        if largest_token < temp:
            largest_token = temp


print("{0}\t{1}".format(largest_token,largest_line))