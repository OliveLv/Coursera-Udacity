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

salesTotal = 0
oldKey = None
maxValue=0
maxKey=None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", salesTotal
        if maxValue<salesTotal:
 	   maxValue=salesTotal
           maxKey=oldKey
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += 1

if oldKey != None:
    #print oldKey, "\t", salesTotal
    if maxValue<salesTotal:
       maxValue=salesTotal
       maxKey=oldKey
print maxKey,"\t",maxValue

