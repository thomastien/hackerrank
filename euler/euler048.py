# Enter your code here. Read input from STDIN. Print output to STDOUT
#import math

total = 0
var = input()

for i in range(1,var+1):
    total = total + pow(i,i, 10000000000)
    # This is multitudes slower, wow
    #total = total + pow(i,i)

#total = sum(pow(n, n, 10**10) for n in range(1,var+1))

print str(int(total))[-10:].lstrip('0')
