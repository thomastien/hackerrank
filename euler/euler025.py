# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import decimal

# We could try to do
sqrt5 = math.sqrt(5)
phi = (1+sqrt5)/2
# However, the floating point precisions would not be sufficient
decphi   = decimal.Decimal('1.6180339887498948482')
decsqrt5 = decimal.Decimal('2.2360679774997896964')

def fibo(n):
    if (n >= 70 ):
        calc = decimal.Context()
        z = calc.power(decphi, decimal.Decimal(n)) /decsqrt5
    else:
        #print "easier version"
        z = math.pow(phi, n)/sqrt5
    #print decimal.Decimal(z)
    #print long(z)
    return long(z)


samples = input()
lengths = {}
max = 0
testcases = []

for x in xrange(samples):
    testcase = input()
    if testcase > max:
        max = testcase
    testcases.append(testcase)
    
# Given constraints, max input was 50000...it's the 23922th fibo #
# A little cheating for speed yeah
max=23923

for i in xrange(max):
    value = str(len(str(fibo(i))))
    dummy = 0
    try:
        # basically, check if key already exists
        # (because if it does, we don't want to replace it)
        dummy = lengths[value]
    except:
        lengths[value] = i


for x in xrange(samples):
    wanted = str(testcases[x])
    print lengths[wanted]
    
'''
Old way
More elaborate, by storing it as e.g.
1.01
1.11
1.21
1.31
1.41
1.51
1.61
2.71 (because 7th fibo # has 2 digits)
2.81
2.91
2.101 <--- notice the problem here when sorted
1.111
3.121 12th fibo # has 3 digits
etc.

The max clause takes too long among other things, and would cause timeout
Please then I had to do the ugly hardcode for 2

for x in xrange(samples):
    wanted = testcases[x]
    #print wanted
    #print lengths[12]
    #print lengths[11]
    #desired = min(k for k in lengths if lengths[k]==wanted)
    try:
        desired = min(k for k in lengths if int(k)==wanted)
        if wanted == 2:
            desired = 2.71
    except:
        #print wanted, ' made it fail'
        raise Exception('blegh', wanted)
    splitstring = str(desired).split('.')
    answer = splitstring[1]
    print answer[:-1]
    #print desired
    
    #value =  round((desired - int(desired)) * 100)
    #print int((value))
  '''
