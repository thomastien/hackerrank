# Enter your code here. Read input from STDIN. Print output to STDOUT


samples = input()

# primes: dictionary of prime numbers
# inputs: list of parameters
allnums = {}
primes = {}
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
        primes[j] = j
        allnums[j] = j
                                  
        for k in range (j+j, cap+1, j):
            #print 'eliminating %i' % k
            allnums[k] = 0
#----------------------------------------------------           
 

if debug:
    print "%i prime numbers were retrieved" % len(primes)
    #print primes
    

testarray = []
curtotal = 0
for value in xrange(cap+1):
    #if value in primes:
    #    curtotal = curtotal + value
    #print value
    try:
        if primes[value]:
            #print "adding ", value, "to ", curtotal
            curtotal = curtotal + value
    except:
        pass
    testarray.append(curtotal)


for value in inputs:
    print testarray[value]
