# Enter your code here. Read input from STDIN. Print output to STDOUT

import operator
import sys
from collections import defaultdict 

# trying to figure out memory error
#print sys.maxsize
#sys.exit(1)

debug = 0

def even(number):
    return number/2

def odd(number):
    return number*3 + 1

def collatz(number):
    if (number%2 == 1):
        number = odd(number)
    else:
        number = even(number)
    return number

def findkey_dict(d):
     # a) create a list of the dict's keys and values
     # b) return the key with the max value  
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]   
    
def findkey_list(d):
    print d
#    return max(xrange(len(d)),key=d.__getitem__)

samples = input()
inputs = []
memoize = []
seen  = defaultdict(list)
cap = 0

for i in xrange(samples):
    val = input()
    inputs.append(val)
    if val > cap:
        cap = val

if debug:
    print cap, ' was  cap'

for i in xrange(1,cap+1):
    if debug:
        print "processing %i :" % i,
        
    # Special exception for 1 due to construction of the while loop
    if i == 1:
        count = 1
    else:
        count = 0
        
    # we don't want i to get polluted
    val= i
    templist = []
    exitval = 0
    
    # if val in seen is way too memory intensive
    # for the size we are dealing with
    try:
        if seen[val]:
            next
    except:
        pass
    
    while val <> 1:
        templist.append(val)
        count=count+1
        if debug:
            print "counter is ", count
        val = collatz(val)
        
        if debug:
            print val, 
        # See if we're at a collatz value seen before, and just take a shortcut
        if val in seen:
            if debug:
                print "we've seen ", val
            # say we counted 2 new one, then reached one where we've seen before with value 6
            # ultimately, we have a final value of 8, but only two are new
            # so we want to save that value: that's how many we need to repopulate in "seen" dict
            exitval = count
            count = count + seen[val]
            break
    
  
    # This is only reached if we didn't "shortcut"
    # So let's iterate backwards, and populate future values
    # e.g. looking up 9 returned 28, 14, 7, 22, 11, 34... etc
    # let's populate 28, 14, 22, 11, 34...
    if count > 1 and exitval < count:
        for j in reversed(xrange(exitval)):
            if debug:
                print j, ' is index <<<', templist, ' new vals <<<', count, ' was count <<<', exitval
                print "we are assigning count of ", count-j, " to ", templist[j]
            z = templist[j]
            if z < 5000000:
                try:
                    seen[z] = count - j
                    #print len(seen)
                except:
                    #print len(seen)
                    pass
#                print z
        
    memoize.append(count)
    seen[i] = count
    if debug:
        print "\n   ", i, ' gave ', count
        
# If memoize was a dict, then can access keys/values   
# print list(memoize.values())

#sys.exit(1)
for i in inputs:
    #print max(memoize.iteritems(), key=operator.itemgetter(1))[0]
    #maxindex = findkey_list(memoize[0:i])
    
    # Because the max(rlist) will return the FIRST element that's max, when there's more than one
    # e.g. if both 18 and 19 had collatz sequence of 21...so we want 19
    # This is why we REVERSE the list, so the first one is just 19
    sublist = memoize[0:i]
    rlist = sublist[::-1]
    if debug:
        print rlist
    #index = max(index())
    #print max(reversed_sublist)
    #print rlist.index(max(rlist)), ' for ', len(rlist)
    answer = i - rlist.index(max(rlist))
    #maxindex=memoize[i:0].argmax()
    if debug:
        print "answer would've been ", answer
    else:
        print answer
 
    
    

    
    
