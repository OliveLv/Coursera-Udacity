#!/usr/bin/python

# a MapReduce program that would process the forum_node data and output the length of the post and the 
# average answer(just answer,not comment)length for each post.

import sys,re,csv

flag=False
reader=csv.reader(sys.stdin,delimiter='\t')
for line in reader:
    if flag and len(line)==19£º
        if line[5]=="question":
            id=line[0]
            type="A"
        if lien[5]=="answer"£º
            id=line[7]
            type="B"
        if line[5]=="question" or line[5]=="answer":
            print "{0}\t{1}\t{2}".format(id,type,len(line[4]))
    if not flag:
        flag=True