#!/usr/bin/python

#We are interested seeing what are the top tags used in posts.

#Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
import sys
import csv

flag=False
reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if flag and len(line)==19:
  	res=line[2].split(" ")
	for val in res:
       	    print "{0}\t{1}".format(val,line[5])
    if not flag:
	flag=True