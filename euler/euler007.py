# Enter your code here. Read input from STDIN. Print output to STDOUT


import math
import pprint
from collections import defaultdict

samples = input()

# primes: dictionary of prime numbers
# inputs: list of parameters
allnums = {}
primes = []
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
    inputs.append(targetval)


# Arbitrary...could do this knowing the input limitations
cap = 120000
if debug:
    print "using a cap of %i to populate prime number list" % cap
#print cap


#----------------------------------------------------
# Create a dictionary of primes
# Basically the sieve of eratosthenes
for j in range(2, cap +1):
    if j in allnums:
        # already seen
        #print "already seen %i" % j
        continue
    else :
        primes.append(j)
        allnums[j] = j
        
#        for elem in inputs:
#            isfactor = lambda elem, j: elem%j==0
#            if isfactor(elem, j):
#                primes.append(j)
                              
        for k in range (j+j, cap, j):
            #print 'eliminating %i' % k
            allnums[k] = 0
#----------------------------------------------------           
 
#pprint.pprint(primes)    
if debug:
    print "%i prime numbers were retrieved" % len(primes)
    
for i in inputs:
   # off by one because primes array started at 0
    if debug:
        print "the %i th prime number is %i" % (i, primes[i-1])
    else:
        print primes[i-1]

