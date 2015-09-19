#!/usr/bin/python
import sys

oldKey=None
postLen=0
ansLen=0
s=0
for line in sys.stdin:
    data_mapped=line.strip().split('\t')
    if len(data_mapped)!=3:
        continue
    thisKey,thisType,thisValue=data_mapped
    if oldKey and oldKey!=thisKey:
        avg=0
        if s!=0:
            avg=float(ansLen)/s
        print "{0}\t{1}\t{2}".format(oldKey,postLen,avg)
        s=0
        ansLen=0
    if thisType=="A":
        postLen=int(thisValue)
    if thisType=="B":
        ansLen+=int(thisValue)
        s+=1
    oldKey=thisKey
if oldKey!=None:
    avg=0
    if s!=0:
        avg=float(ansLen)/s
    print "{0}\t{1}\t{2}".format(oldKey,postLen,avg)