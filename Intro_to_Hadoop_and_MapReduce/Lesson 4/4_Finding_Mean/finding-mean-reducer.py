#!/usr/bin/python

# a MapReduce program that processes the purchases.txt file and outputs mean of sales for each weekday.

import sys

salesTotal = 0
oldKey = None
num=0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal/num
        oldKey = thisKey;
        salesTotal = 0
	num=0

    oldKey = thisKey
    salesTotal += float(thisSale)
    num+=1

if oldKey != None:
    print oldKey, "\t", salesTotal/num

