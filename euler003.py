# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import pprint
from collections import defaultdict

samples = input()

# primes: dictionary of prime numbers
# inputs: list of parameters
primes = {}
#lpfs = {}
lpfs = defaultdict(list)
inputs = []

#pp = pprint.PrettyPrinter;
    
def isFactor(n,d):
    if n%d == 0:
        return True
    else:
        return False

    
for i in range(0,samples):
    targetval = input()
    #inputs.insert(0,targetval)
    inputs.append(targetval)

print max(inputs) 
highest = max(inputs)
    
cap = int(math.sqrt(highest))
# This would cause Memory error
#cap = highest/2

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
                print "found %i for %s" % (j, elem)
                lpfs[elem].append(j)
                              
        for k in range (j+j, cap, j):
            #print 'eliminating %i' % k
            primes[k] = 0
    
#pprint.pprint(primes)

for item in inputs:
    try:
        print "%i larges prime factor was %s" % (item, lpfs[item])
    except:
        print "%i is its own largest factor" % item
       
#print max(primes, key=lambda i: primes[i])
