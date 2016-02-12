
allnums = {}
primes = {}

debug =0

val = input()


#----------------------------------------------------
# Create a dictionary of primes
# Basically the sieve of eratosthenes
for j in range(2, val+1):
    if j in allnums:
        # already seen this, skip
        continue
    else :
        primes[j] = j
        allnums[j] = j
                                  
        for k in range (j+j, val+1, j):
            #print 'eliminating %i' % k
            allnums[k] = 0
#----------------------------------------------------           

    
if debug:
    print "%i prime numbers were retrieved" % len(primes)
    print primes

  
def cantruncate(n):
    x = str(n)
    
    # Per condition
    if n in (2,3,5,7):
        return False
    
    for i in xrange(1,len(x)):
        left = x[i:]
        right = x[:len(x)-i]
        
        if primes[int(left)] and primes[int(right)]:
            if debug:
                print left, ' and ', right, 'passed'
            pass
        else:
            print 'one is no good'
            return False

    if debug:
        print "Truncatable", x
    return True
      
    
  
curtotal = 0
for value in xrange(val+1):
    try:
        if primes[value]:
            if cantruncate(value):
                curtotal = curtotal + value
    except:
        pass
    


print curtotal
