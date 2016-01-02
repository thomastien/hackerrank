# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import decimal


# We could try to do
sqrt5 = math.sqrt(5)
phi = (1+sqrt5)/2
# However, the floating point precisions would not be sufficient
decphi   = decimal.Decimal('1.6180339887498948482')
decsqrt5 = decimal.Decimal('2.2360679774997896964')

def isPerfectSquare(n):
    root = long(math.sqrt(n))
    #print "root was %s for n" % str(root), str(n)
    squared = root * root
    #print "squared = %s" % str(squared)
    return (root*root == n)
    
def isfibo(n):
    # Computers don't handle rounding of logarithms very well, e.g. 
    # 987 is a fibonacii #, 986 is not
    # BUT, findfibo will give 15.887 for 986, 15.9999 for 987
    #  how can I determine accurately when I should round?
    # seems best way is just check IF a number is a fibonacci 
    if isPerfectSquare((5*n*n)+4) or isPerfectSquare((5*n*n)-4):
        return True
    else:
        return False
    
def findfibo(x):
    # Position     1 2 3 4  5  6  7  8  9  10  11  12  13  14   15  16
    #-----------------------------------------------------------------
    # Fibonacci #s 1 1 2 3  5  8 13 21 34  55  89 144 233 377  610 987
    # Sums         1 2 4 7 12 20 33 54 88 143 232 376 609 986 1596
    # Sums evens   0 0 2 2  2 10 10 10 44  44  44 188 188 188  798
    # f(n) The nth fibonacii # can be expressed phi^n / sqrt (5)
    # S(n) The nth sum is always f(n+2)-1
    # SE(n) is S(n)/2, provided n%3 ==0.  If n%3 <> 1, use S(n') where n' = next lowest multiple of 3
    #
    # Within parameters of the problem, they wanted SUM of all EVEN fibonacii #s <= X
    # So we want to know n where f(n) >= X
    # phi^n / sqrt (5) >= X
    # X sqrt(5) <= phi^n
    # ln(X sqrt(5)) <= N ln (phi)
    # so N >= ln (x sqrt(5))/ln(phi)
    # Testing cases, 
    #  natural log of (88*(squart root of 5))/natural log of phi = 10.97 in Google
    #  natural log of (89*(squart root of 5))/natural log of phi = 11.00005 
    #  natural log of (986*(squart root of 5))/natural log of phi = 15.9997
    # Verified this works
    #print "assessing %s" % x
    
    # This is less precise than the global one, but we don't need that precision here
    #if isfibo(x):
    if (0==1):
        #print "is fibo"
        return round(math.log(x*sqrt5)/math.log(phi))
    else:
        #print "is not fibo"
        return long(math.log(x*sqrt5)/math.log(phi))
    

def fibo(n):
    if (n >= 70 ):
        calc = decimal.Context()
        z = calc.power(decphi, decimal.Decimal(n)) /decsqrt5
    else:
        #print "easier version"
        z = math.pow(phi, n)/sqrt5
    #print decimal.Decimal(z)
    return int(z)
    
cases = input()
seen = {}
for i in range(1,cases+1):
    n = input()
        
    fiboarg = findfibo(n)
    #print "fiboarg was %s" % str(fiboarg)
    if (fiboarg %3 != 0):
        fiboarg = fiboarg - fiboarg%3
    
    if fiboarg in seen:
        #print "seen you before %s" % fiboarg
        print seen[fiboarg] 
    else:
        # See comments in findfibo
        # SE(n) is S(n)/2, provided n%3 ==0.  If n%3 <> 1, use S(n') where n' = next lowest multiple of 3
        #print fiboarg
        answer = fibo(fiboarg+2)/2
        print answer 
        #print fiboarg
        seen[fiboarg] = answer
    
