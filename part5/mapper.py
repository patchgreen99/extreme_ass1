#!/usr/bin/python

import sys
import heapq

h = []
counter = 0

for line in sys.stdin:
    line = line.strip()
    sequence, frequency = line.split("\t", 1)
    if (heapq.nsmallest(1,h) < frequency):
        heapq.heappop(h)
        counter-=1

    if (counter < 20):
        heapq.heappush(h, (frequency,sequence))
        counter+=1

for frequency,sequence in h:
    print ("{0}\t{1}".format(frequency,sequence))