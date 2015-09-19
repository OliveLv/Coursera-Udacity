#!/usr/bin/python

# Format of each line is:
# ip id username time zone method path reques status  size 
#
# Find the most popular file on the website: that is, the file whose path occurs most often in access_log.
# Your reducer should output the file's path and the number of times it appears in the log.
# IMPORTANT: Some pathnames in the log begin with "http://www.the-associates.co.uk".Be sure to remove
# the portion "http://www.the-associates.co.uk" from pathnames in your mapper so that all occurrences of 
# a file are counted together.

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip,id,username,time,zone,method,path,request,status,size = data
        if path.startswith("http://"):
	   path="/"+'/'.join(path.split("/")[3:])
        print "{0}\t{1}".format(path, method)

