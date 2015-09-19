#!/usr/bin/python

# a MapReduce program which will display the number of hits for each different file on the Web site.

import sys

oldKey=None
hits=0
for line in sys.stdin:
	data_mapped=line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	thisKey,thisValue=data_mapped
	if oldKey and oldKey!=thisKey:
		print oldKey,"\t",hits
		hits=0
	oldKey=thisKey
	hits+=1
if oldKey!=None:
	print oldKey,"\t",hits