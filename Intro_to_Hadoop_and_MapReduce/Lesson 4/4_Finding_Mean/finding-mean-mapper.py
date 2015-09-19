#!/usr/bin/python

# a MapReduce program that processes the purchases.txt file and outputs mean of sales for each weekday.

import sys
import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(datetime.datetime.strptime(date,'%Y-%m-%d').weekday(), cost)

