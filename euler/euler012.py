# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import collections

samples = input()

debug=0
cap=45000  # arbitrary yes, this was picked via trial & error will handle the max test case N=1000

def triangulate(n):
    return ((n**2)+n) / 2
    
def numfactors(n):
    ceiling = int(math.sqrt(n))
    factors = {}
    for i in xrange(1,ceiling+1):
        quotient, remainder = divmod(n,i)
        if remainder==0:
            factors[quotient] = 1
            factors[i] = 1
    
    if debug:
        print factors, len(factors)
    return len(factors)
    
factors = {}
answers={}

# First we count the # of factors for all numbers from 1..cap
for i in xrange(1,cap):
    factors[i] = numfactors(i)
    
# How this works
# We know triangular #s sum = N^2 + N /2...  or (N)(N+1)/2
# It turns out, for where N is EVEN
# The # of factors can be reduced to (# of factors for N/2) * (# of factors for N+1)
#
# If N is ODD
# The # of factors can be reduced to (# of factors for N+1/2) * (# of factors for N)
#
# for e.g. N=9, which givers triangular # of 45
# The # of factors for 45 (1,3,5,9,15,45)
# is same as # of factors for N+1/2 (5, which gives 1, 5 or 2 total) * # of factors for 9 (1, 3, 9 = 3 total)  

for i in xrange(1,cap):
    factor1 = factor2 = 0
    
    if i%2==0:
        factor1 = i/2
        factor2 = i+1
    else:
        factor1 = (i+1)/2
        factor2 = i
        
    answer = factors[factor1] * factors[factor2]
    if debug:
        print i, ' got ', answer
        #print 'doing it the hard way would get', numfactors(number)
    number=triangulate(i)
    answers[number] = answer

fixed = collections.OrderedDict(sorted(answers.items()))  

if debug:
    print fixed.keys()

for i in xrange(samples):
    t = input()
    try:
        print min(k for k in fixed.keys() if fixed[k]>t)
    except ValueError as e:
        print e
        raise BaseException("you may want to raise the cap from %i to fix this" % cap)
