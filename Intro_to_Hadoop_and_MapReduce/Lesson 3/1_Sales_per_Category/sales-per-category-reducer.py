#!/usr/bin/python

# Problem
# Find the total sales value across all the stores,and the total number of sales,assume there is only one reducer.
# Sales per category

import sys
oldKey=None
salesTotal=0
salesNum=0
salesPerCat=0
for line in sys.stdin:
	data_mapped=line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	thisKey,thisSale=data_mapped
	if oldKey and oldKey!=thisKey:
		print oldKey,"\t",salesPerCat
		salesPerCat=0
		oldKey=thisKey
	oldKey=thisKey
	salesTotal+=float(thisSale)
	salesPerCat+=float(thisSale)
	salesNum+=1
if oldKey!=None:
	print oldKey,"\t",salesPerCat

print "salesTotal: ",salesTotal
print "salesNum: ",salesNum