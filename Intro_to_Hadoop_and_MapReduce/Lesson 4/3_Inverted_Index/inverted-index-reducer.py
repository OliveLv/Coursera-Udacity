#!/usr/bin/python

# a MapReduce program that creates an index of all words that can be find in the body of a forum
# post and node id they can be found in.
# Do not parse the HTML. Just split the text on all whitespaces as well as the following charactors:
# .,!?:;"()<>[]#$=-/

import sys

df=1
cf=0
oldKey = None
oldValue=None
index=""

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

