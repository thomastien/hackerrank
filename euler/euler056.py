# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
max = 0

for a in xrange(1,n+1):
    for b in xrange(1,n+1):
        result = map(int, list(str(a**b)))
        value = sum(result)
        if value > max:
            max = value
print max
