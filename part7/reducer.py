#!/usr/bin/python

import sys
import math

start = True

for line in sys.stdin:
    line = line.strip()
    input = line.split(".")

    # Remember that Hadoop sorts map input by key reducer takes these keys sorted
    if input[1] == '1':
        print "(" + input[2] + "," + input[3] + ") ",
    else:
        if start:
            print input[2] + " --> ",
            start = False
        else:
            print '\n'+input[2]+" --> ",



