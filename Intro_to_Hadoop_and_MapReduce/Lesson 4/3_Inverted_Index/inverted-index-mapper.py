#!/usr/bin/python

# a MapReduce program that creates an index of all words that can be find in the body of a forum
# post and node id they can be found in.
# Do not parse the HTML. Just split the text on all whitespaces as well as the following charactors:
# .,!?:;"()<>[]#$=-/

import sys
import re
import csv

flag=False
reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for data in reader:
    #data = line.strip().split("\t")
    #data=line
    if len(data) >=5:
        id=data[0]
        body=data[4]
        lines=body.split(" ")
        for line in lines:
	     words=re.split('[.,!?:;()<>\[\]$#=\-/\"]', line)
             for word in words:
        	 if word==" " or len(word)==0:
	            continue
		 #writer.writerow("{0}\t{1}".format(word,id))
                 if "fantastic" in word.lower():
	            print "{0}\t{1}".format(word.lower(),id)
      #  print "{0}\t{1}".format(store, cost)

