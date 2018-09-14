#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    try:
        type, id, identifier, value = line.split()
        print ("{0}.{1}.{2}.{3}".format(id, "1", identifier, value))
    except:
        type, id, identifier = line.split()
        print ("{0}.{1}.{2}".format(id, "0", identifier))
