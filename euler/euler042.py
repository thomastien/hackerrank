# Enter your code here. Read input from STDIN. Print output to STDOUT


# so triangle number formula is (N^2+N / 2)
# So we need to know if a number say Z fits the formula
# 2Z = N^2+N
# N^2+N - 2Z = 0
# within the quadratic formula, this gives
# A=1
# B=1
# C=-2Z
# so quadratic formula being -b +/- sqrt(b^2-4AC)  all over 2
# -1 +/- sqrt (1 +8Z) all over 2
# So a number Z is a triangular number, if
# (sqrt(8Z+1) -1) /2 is an integer
import math

def istriangle(z):
    answer = (math.sqrt(z*8 + 1) -1) / 2
    #print z, " gave ", answer
    if answer == int(answer):
        return int( answer )
    else:
        return -1

samples = input()
    
for i in xrange(samples):
    question = input()
    print istriangle(question)
