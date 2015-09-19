#!/usr/bin/python

# We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

#As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

import sys
import re
import csv
import time

flag=False
reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for line in reader:
    if flag and len(line)==19:
	if line[5]=="question":
	   print "{0}\t{1}".format(line[0],line[3])
	else:
	   print "{0}\t{1}".format(line[7],line[3])
    if not flag:
	flag=True
