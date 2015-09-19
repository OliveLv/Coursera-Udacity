#!/usr/bin/python

# Format of each line is 
# data time store name item-description cost method-of-payment

# Problem
# breaking down the sales by store

import sys

for line in sys.stdin:
	data=line.strip().split("\t")
	if len(data)==6:
		data,time,store,item,cost,payment=data
		print "{0}\t{1}".format(store,cost)