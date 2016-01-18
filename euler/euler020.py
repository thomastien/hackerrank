# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

samples = input()

for i in xrange(samples):
    # can do this in one line, but not great for readability
    # print sum ( map(int, list(str(math.factorial(input())))))
    val = input()
    answer = math.factorial(val)
    answer = list(str(answer))
    answer = map(int, answer)
    print sum(answer)
