#!/usr/bin/python
import sys
oldKey=None
oldValue=None
max=0
list=[]
s=0
for data in sys.stdin:
    line=data.strip().split('\t')
    if len(line)!=2:
        continue
    thisKey,thisValue=line
    if oldKey and oldKey!=thisKey:
        if max<s:
            list=[]
            max=s
        if max==s:
            list.append(oldValue)
        for val in list:
            print "{0}\t{1}".format(oldKey,val)
        list=[]
        s=0
        max=0
        oldValue=None
    if oldValue and oldValue!=thisValue:
        if max<s:
            list=[]
            max=s
        if max==s:
            list.append(oldValue)
        s=0
    s+=1
    oldKey=thisKey
    oldValue=thisValue
if oldKey!=None:
    for val in list:
        print "{0}\t{1}".format(oldKey,val)
          