#!/usr/bin/python

import sys

prev_sequence = ""
value_total = 0
sequence = ""

for line in sys.stdin:  # For ever line in the input from stdin
    #line = line.strip()  # Remove trailing characters
    sequence, value = line.split("\t")
    value = int(value)

    # Remember that Hadoop sorts map input by key reducer takes these keys sorted
    if prev_sequence == sequence:
        value_total += value
    else:
        if prev_sequence:  # write result to stdout
            print("{0}\t{1}".format(prev_sequence, value_total))
        value_total = value

    prev_sequence = sequence

if prev_sequence == sequence:  # Don't forget the last key/value pair
    print("{0}\t{1}".format(prev_sequence, value_total))

