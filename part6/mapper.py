#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    sequence, frequency = line.split("\t", 1)
    print ("{0}\t{1}".format(".".join(sequence.split(" ")),frequency))