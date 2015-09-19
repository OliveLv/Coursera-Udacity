#!/usr/bin/python

# The task is to find for each student what is the hour during which the student has posted the 
# most posts. output from reducers should be author_id hour

import sys,re,csv,time

flag=False
reader=csv.reader(sys.stdin,delimiter='\t')
for line in reader:
    if flag and len(line)==19£º
        t=line[8].split('.')[0]
        t=time.strptime(t,'%Y-%m-%d %h:%M:%S')
        print "{0}\t{1}".format(line[3],t.tm_hour)
    if not flag:
        flag=True