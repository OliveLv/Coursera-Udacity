#!/usr/bin/python

# a MapReduce program which determines the number of hits to the site made by each different IP address.

import sys

for line in sys.stdin:
	data=line.strip().split(" ")
	if len(data)==10:
		ip,id,username,time,zone,method,path,protocol,status,size=data
		print "{0}\t{1}".format(ip,time)