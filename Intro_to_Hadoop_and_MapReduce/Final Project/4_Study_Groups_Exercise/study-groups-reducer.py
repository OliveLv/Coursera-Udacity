#!/usr/bin/python

#We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

#As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

import sys

oldKey=None
list=[]
for data in sys.stdin:
    line=data.strip().split('\t')
    #print len(line)
    if len(line)!=2:
	continue
    thisKey,thisValue=line
    if oldKey and oldKey!=thisKey:
        print "{0}\t[{1}]".format(oldKey,",".join(list))
  	list=[]
    oldKey=thisKey
    list.append(thisValue)	
if oldKey!=None:
    print "{0}\t[{1}]".format(oldKey,",".join(list))			    
