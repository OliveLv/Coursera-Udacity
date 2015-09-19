#!/usr/bin/python

# Problem
# Find the monetary value for the highest individual sale for each separate store.

import sys

oldKey=None
maxValue=0
for line in sys.stdin:
	data_mapped=line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	thisKey,thisValue=data_mapped
	if oldKey and oldKey!=thisKey:
		print oldKey,"\t",maxValue
		maxValue=0
	oldKey=thisKey
	maxValue=max(maxValue,float(thisValue))
if oldKey!=None:
	print oldKey,"\t",maxValue