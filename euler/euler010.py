# Enter your code here. Read input from STDIN. Print output to STDOUT




samples = input()

# primes: dictionary of prime numbers
# inputs: list of parameters
allnums = {}
primes = []
inputs = []

debug =0



cap = 0
for i in xrange(samples):
    val = input()
    if val > cap:
        cap = val
    inputs.append(val)

if debug:
    print "using a cap of %i to populate prime number list" % cap


#----------------------------------------------------
# Create a dictionary of primes
# Basically the sieve of eratosthenes
for j in range(2, cap+1):
    if j in allnums:
        # already seen this, skip
        continue
    else :
        primes.append(j)
        allnums[j] = j
                                  
        for k in range (j+j, cap+1, j):
            #print 'eliminating %i' % k
            allnums[k] = 0
#----------------------------------------------------           
 

if debug:
    print "%i prime numbers were retrieved" % len(primes)
    #print primes

memoize = {}

answer  = 0
largest = 0
ceiling = 0

for value in sorted(inputs):
    if memoize.get(value, 0) > 0:
        if debug:
            print "skiiping!"
        next
        
    try:
        ceiling = max(k for k in memoize if k<=value)
    except:
        ceiling = 0 
    
    
    if ceiling in memoize:
        if debug:
            print "I've seen up to ", ceiling, 'before'
            print "going to add ", memoize[ceiling]
        d = [k for k in primes if k<=value and k>ceiling]
        answer = sum(d) + memoize[ceiling]
    else:
        d = [k for k in primes if k<= value]
        answer = sum(d)

    memoize[value] = answer


for value in inputs:
    print memoize[value]
    
  
