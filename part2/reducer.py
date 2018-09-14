#!/usr/bin/python

import sys

prev_line = ""
line = ""
matched = False

for line in sys.stdin:  # For ever line in the input from stdin
    temp = line[:-1]


    # Remember that Hadoop sorts map input by key reducer takes these keys sorted
    if prev_line == temp:
        matched = True
    else:
        if prev_line and not matched:  # write result to stdout
            print("{}".format(prev_line))
        matched = False

        prev_line = temp

if not matched:  # Don't forget the last key/value pair
    print("{}".format(prev_line))