# Enter your code here. Read input from STDIN. Print output to STDOUT
# 2520 = 1 * 2 * 5 * 9 * 7 * 4
# becasuse 2.4.4 = 8
# 2.(part of 9) = 6
# etc...so those subcomponents are accounted for
# so given a range
# 1 2 3 4 5 6 7 8 9
# first I retrieve all the primes, 1 2, 3, 5, 7
# BUT that's not sufficient!!  I need then check the non-primes to see if they can be generated from the primes,
#  e.g. 4 couldn't be by 2 alone, so I need to make it 2x2
#  6 can be 2x3, so skipped
#  8 can't be 2x2, so a 3rd two
#  9 can't be by 3 alone, so a 2nd 3
#  so that's how it actually is 1 * 5 * 8 * 7 * 9...

# alternate algo
# ok start with 2, find highest power that fits <= # = 8
# 3, then we got 9
# 4 not prime
# 5 prime
# 6 not prime
# 7 prime
# 8 not prime
# 9 not prime
# so we end with 8*9*5*7 = 360*7 = 2520 <-- this is it I think


# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import pprint
from collections import defaultdict

samples = input()

# primes: dictionary of prime numbers
# inputs: list of parameters
primes = {}
lpfs = defaultdict(list)
inputs = []
debug = 0

#pp = pprint.PrettyPrinter;
    
def isFactor(n,d):
    if n%d == 0:
        return True
    else:
        return False
    
def expand(factor, orig):
    value = factor
    while (value * factor <= orig):
        value = value * factor    
    return value

    
for i in range(0,samples):
    targetval = input()
    #inputs.insert(0,targetval)
    inputs.append(targetval)

if debug:
    print max(inputs) 

cap = max(inputs)
    
for j in range(2, cap+1 ):
    if j in primes:
        # already seen
        #print "already seen %i" % j
        continue
    else :
        primes[j] = j
        
        for elem in inputs:
            if isFactor(elem, j):
                #print "found %i for %s" % (j, elem)
                lpfs[elem].append(j)
                              
        for k in range (j+j, cap+1, j):
            #print 'eliminating %i' % k
            primes[k] = 0
#----------------------------------------------------           
    
if debug:
    pprint.pprint(primes)


for item in inputs:
    value = 1
    for i in range(2,item+1):
        if debug:
            print "%i vs %i" % (i, primes[i])
        if primes[i] == i:
            value = value * expand(i, item)
    print value
       
#print max(primes, key=lambda i: primes[i])

