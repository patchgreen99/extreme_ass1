#!/usr/bin/python

import sys
import math

w = 0
c = 0

current_prefix = ""
last_prefix = ""

for line in sys.stdin:
    line = line.strip()
    thing, frequency = line.split("\t", 1)

    current_prefix = " ".join(thing.split(".")[:-1])
    temp = int(frequency)
    
    if last_prefix == current_prefix:
            w += temp * math.log(temp, 2)
            c += temp
    else:
        if last_prefix:  # write result to stdout
            print("{0}\t{1}".format(last_prefix, (-w/float(c))+math.log(c,2)))
            w = temp * math.log(temp, 2)
            c = temp

    last_prefix = current_prefix

if last_prefix == current_prefix:  # Don't forget the last key/value pair
    print("{0}\t{1}".format(last_prefix, (-w/float(c))+math.log(c,2)))

