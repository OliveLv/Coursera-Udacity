#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
user_info=None
oldKey=None
for line in sys.stdin:
    if line[1]=="A":
        user_info=line[2:]
    if line[1]=="B":
        print line[2:],"\t",user_info

        