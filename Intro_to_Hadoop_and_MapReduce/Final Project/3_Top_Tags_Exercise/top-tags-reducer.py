#!/usr/bin/python

#We are interested seeing what are the top tags used in posts.

#Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
import sys,Queue
from operator import itemgetter
oldKey=None
total=0
q=Queue.PriorityQueue(10)
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey,thisValue = data_mapped
    if oldKey and oldKey!=thisKey:
	if q.full():
	   q.get()
	q.put((total,oldKey))
	total=0 
    oldKey=thisKey
    if thisValue=="question":
	total+=1
	   

if oldKey != None:
    if q.full():
	q.get()
    q.put((total,oldKey))
f=lambda (k,v):(v,k)
list=[]
while not q.empty():
    list.append(f(q.get()))
list=sorted(list,key=itemgetter(1,0),reverse=True)
for key,value in list:
    print "{0}\t{1}".format(key,value)

