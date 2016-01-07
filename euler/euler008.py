# Enter your code here. Read input from STDIN. Print output to STDOUT
# brute force seems doable...let's hope not time out
import pprint
samples = input()
debug = 0

def findproduct(value):
    # save some memory, return 0 if see 0
    if '0' in value:
        if debug:
            print 'zero found in %s' % value
        return 0
    
    (array) = list(value)
    #pprint.pprint(array)
    returnval = 1
    for val in array:
        returnval = returnval * int(val)
    
    return returnval
    
for i in range(samples):
    (n,k) = raw_input().split(' ')
    
    T = raw_input()
    if debug:
        print "looking for highest %i digit number in %i digit number: %i" % (int(k), int(n), int(T))
        #print "looking for highest %i digit number in %i digit number: %i" % (int(k,n,T))
    
    currmax = 0
    
    for i in xrange(int(n)-int(k)):
        value = T[i:i+int(k)]
        product = findproduct(str(value))
        if product > currmax:
            currmax = product
          
    
    print currmax
    
