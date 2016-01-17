# Enter your code here. Read input from STDIN. Print output to STDOUT

samples = input()

sum = 0
for i in xrange(samples):
    number = input()
    sum = sum + number
    
sum = str(sum)
print sum[0:10]
