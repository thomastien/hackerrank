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
    
def reduce(orig,factor):
    while (orig%factor ==0):
        orig = orig/factor
    return orig

    
for i in range(0,samples):
    targetval = input()
    #inputs.insert(0,targetval)
    inputs.append(targetval)

if debug:
    print max(inputs) 
highest = max(inputs)
    
cap = int(math.sqrt(highest))
# This would cause Memory error, so we will use sqrt, and rely on the reduce function
#cap = highest/2

#----------------------------------------------------
# Create a dictionary of primes
# Basically the sieve of eratosthenes
for j in range(2, cap ):
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
                              
        for k in range (j+j, cap, j):
            #print 'eliminating %i' % k
            primes[k] = 0
#----------------------------------------------------           
 
    
if debug:
    pprint.pprint(primes)

for item in inputs:
    max = 0
    try:
        if debug:
            print "%i larges prime factor was %s" % (item, lpfs[item])
        mutable_value = item
        for factor in lpfs[item]:
            max = factor
            mutable_value = reduce(mutable_value, factor)
        if debug:
            print "%i was max, last mutable ws %s" % (max, mutable_value)   
        if mutable_value != 1:
            print mutable_value
        else:
            print max
    except:
        print "%i is its own largest factor" % item
       
#print max(primes, key=lambda i: primes[i])
