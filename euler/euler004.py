# Enter your code here. Read input from STDIN. Print output to STDOUT


# Strategy
# Given a #, (assume <=998001)
# Need to verify
# A: number is palindromic
# B: number is product of 3-digit #s
# brute-force could start from 998001, downwards
#  and divide by all #s 100-999, until modulous 0
# STRATEGY TWO (the one used)
# iterate through all products 100-999 * 100-999, note this is 808201 combinations
#  store this in a dictionary, and just locate the largest one < N

import pprint

debug = 0

def isPalin(x):
    x = str(x)
    revx = x
    if revx[::-1] == x:
        return True
    else:
        return False

# Doesn't need to be a dict, will use a list
#allpalins ={}
allpalins = []
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if isPalin(product):
            #allpalins[product] = product
            allpalins.append(product)
            

if debug:
    allpalins.sort()
    pprint.pprint(allpalins)       
        
n = input()

for i in range(1,n+1):
    # note input evaluates, raw_input keeps as is
    # so use raw_input if it can be a string.  In this case it's unnecessary, but
    #  just noted (plus done) as an exercise
    x = int(raw_input())
    #print max(allpalins, key=lambda x: allpalins[i] < x)
    
    index = max(k for k in allpalins if k <=x)
    if debug:
        print "Highest palindronmic product less than %i was %i" % (x,index)
    else:
        print index
    #print allpalins[index]
    
