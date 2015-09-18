#!/usr/bin/python

import sys

df=1
cf=0
oldKey = None
oldValue=None
index=""
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped
    if oldKey==None:
	index+=thisValue+","
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", df,"\t",cf,"\t",index
        oldKey = thisKey;
        oldValue=thisValue
        df=1
        cf=0
        index=thisValue+","

    oldKey = thisKey
    if oldValue!=thisValue:
	oldValue=thisValue
	df+=1
        index+=thisValue+","
    cf+=1
   # index+=thisValue+","
    

if oldKey != None:
    print oldKey, "\t", df,"\t",cf,"\t",index

