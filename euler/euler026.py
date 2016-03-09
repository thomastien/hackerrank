# Enter your code here. Read input from STDIN. Print output to STDOUT
import decimal
from decimal import *

# If this is set too low, you get truncated results
# e.g. earlier this was set at 4k, and we got a bunch of wrong answers capped at 3906 
getcontext().prec = 10000

samples = input()
inputs = []
cap = 0
debug =0

# sets the cap, so we don't have to iterate through the loop multiple time
# e.g. if inputs were 1, 9, 25...we only want to iterate through the 25, and in the process
#      we would already have the answers for 1 and 9
for i in xrange(samples):
    value = input()
    inputs.append(value)
    if value > cap:
        cap = value


# Given a number, say 1/7 which 0.142857142857142857
# this function needs to be able to detect "142857" = returns 6, which is the answer
def findrepeat(number):
    notfound = True
    
    cut=0
    max=len(number)
    
    # This is an arbitrary cap, though if a number stopped at 100, safe to say it was non-repeating?
    if max < 100:
        return max
 
    while notfound:
        cut=cut+1
        
        x = number[0:cut]
        y = number[cut:cut*2]
        # so for 1/7 for instance, we will
        # compare 1 vs 4
        # compare 14 vs 28
        # compare 142 vs 857
        # compare 1428 vs 5714
        # compare 14285 vs 71428
        # compare 142857 vs 142857 < -- found it
        if y == x:
            # We are not out of the woods yet
            # we can have 33333333333, this one just because 3333=3333, doesn't mean answer is 4, it's 1, 3 repeated adnauseum
            # or say 3312334242358799999
            double=cut*2
            x2=number[0:double]
            y2=number[double:double*2]
            if cut > 10 or y2 == x2:
                # now we know it's legit
                notfound = False
            else:
                # false alarm, keep going
                pass
        if cut>max:
            break
    
    #if cut == 3956 and number > 1979:
    #    # impossible result
    #    getcontext().prec = int(number * 2) + 100
    #    result = str(decimal.Decimal(1)/i)
    #    result = result[50:]
    #    repeats = findrepeat(result)
    #    #print 'in here'
    #    getcontext().prec =4000       
    return cut    
        
answers={}
for i in xrange(1,cap):
    # This does NOT work, technically!  if we just assign 0 if divisble by two
    # for instance, 6 is a multiple of 2, it's not repeating 0, but 1s...
    # it only works for powers of 2, not multiples of
    # although, within the parameters of this problem (find the lowest)
    # since answers[6] = answers[12] = answers[24] = answers[48] ...etc, seems hould be ok
    #if i%2 == 0:
    if i%2 == 0:
        answers[i]=0
    elif i>3 and i%3 == 0:
        answers[i]=0
    elif i>5 and i%5 == 0:
        answers[i]=0
    elif i>7 and i%7 == 0:
        answers[i]=0
    elif i>11 and i%11 == 0:
        answers[i]=0
    elif i>13 and i%13 == 0:
        answers[i]=0
    elif i>17 and i%17 == 0:
        answers[i]=0
        #result = str(decimal.Decimal(1)/i)
        #print result
        #answers[i] = len(result) -2
        #print result, 'got', answers[i]
        #answers[i] = 0
    else:
        #if i>2000:
        #    getcontext().prec = i*2
        result = str(decimal.Decimal(1)/i)
        # ok, this is a bit hacky, but this should safely prevent false hits
        result = result[50:]
        repeats = findrepeat(result)
        #if debug or (i==1709 or i==1979):
        if debug and i > 1700:
            #print i, 'got ', result,
            print i, repeats
        answers[i] = repeats
    
for i in inputs:
    #print i
    try:
        #print max(k for k in answers.keys())
        # find the answer with the longest recurring cycle
        # remember criteria says "smallest d < N", so <, not <=
        maxingroup= max(answers[k] for k in answers.keys() if k < i)
        # if there's more than one, want the SMALLEST one
        correct  = min(k for k in answers.keys() if answers[k] == maxingroup and k < i)
        if debug:
            print correct, 'was the answer with a length of', answers[correct]
        else:
            #pass
            print correct
    except:
        print 'fail'
        raise BaseException("did not work")
