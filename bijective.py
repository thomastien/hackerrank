#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Bijective function, basically counts uniqueness and 1-to-1 mapping
# Example, 6 [1 2 3 4 5 6] = YES
#          6 [1 2 3 4 5 5] = NO
#          5 [1 2 3 4 5 6] = NO
#   20 [20 19 18 17 16 15 14 13 12 11 1 2 3 4 5 6 7 8 9 10] = YES
#   Note this case it what makes a simple .count not work, because 1 appears in 11, 12, 13 etc too...
#     Hence had to use Counter, which's supposedly 2X faster than count anyway
from collections import Counter
size = raw_input()
vals = raw_input()

#print len(vals.split())
#print size
returnval = 'YES'
z = Counter(vals.split())

if int(size) == len(vals.split()):
    for i in vals.split():
        if z[i] >1:
            #print vals.count(i)
            #print i
            returnval = 'NO'
            break
else:
    returnval = 'NO'

print returnval

