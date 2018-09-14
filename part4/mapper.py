#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()

    last_sequence = ""
    sequence = ""
    stripped = []

    for token in tokens:
        stripped.append(token.strip())

    for i in range(len(stripped)-2):
        sequence = " ".join(stripped[i:i+3])

        print("{0}\t{1}".format(sequence, 1))