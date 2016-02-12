# Enter your code here. Read input from STDIN. Print output to STDOUT

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

  
def circular(n):
    x = str(n)
    
    
    for i in xrange(1,len(x)):
        x = x[1:] + x[0]
        
        if primes[int(x)]:
            #print x, "is prime"
            pass
        else:
            # interestingly this is never reached if primes[int(x)] does not exist
            print 'failed on', x
            return False
        
        
    if debug:
        print "Circular", x
    return True
      
    
  
curtotal = 0
for value in xrange(val+1):
    try:
        if primes[value]:
            if circular(value):
                curtotal = curtotal + value
    except:
        pass
    


print curtotal
