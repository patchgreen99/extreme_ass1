#!/usr/bin/python

import sys

counter = 0

for line in sys.stdin:  # For ever line in the input from stdin
    line = line.strip()
    frequency, sequence = line.split("\t", 1)

    print ("{0}\t{1}".format(frequency, sequence))