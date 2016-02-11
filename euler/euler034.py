# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = input()
fact = {}

for i in xrange(10):
    fact[i] = math.factorial(i)

def isCurious(number):
    array = list(str(number))
    sum = 0
    
    for elem in array:
        sum = sum + fact[int(elem)]
    #print number, ' got ', sum
    if sum%number == 0:
        return True
    else:
        return False
    
grandtotal = 0
for i in xrange(10,n):
    if isCurious(i):
        #print i, 'is curious'
        grandtotal = grandtotal + i

print grandtotal
