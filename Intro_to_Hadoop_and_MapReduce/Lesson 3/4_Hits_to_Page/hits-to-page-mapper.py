#!/usr/bin/python

# a MapReduce program which will display the number of hits for each different file on the Web site.

import sys
for line in sys.stdin:
	data=line.strip().split(" ")
	if len(data)==10:
		ip,id,username,time,zone,method,path,protocol,status,size=data
		print "{0}\t{1}".format(path,status)