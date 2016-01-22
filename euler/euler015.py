# Enter your code here. Read input from STDIN. Print output to STDOUT
#  So, lattice paths are supposed to be using the central binomial coefficient,
#  see https://en.wikipedia.org/wiki/Central_binomial_coefficient
#  basically 2N! / (n! * n!)  : yes, very similar to the catalan # for calculating permutations in a binary tree,
#   except that one's denominator would be n! (n+1)!  ... this works for situations where M = N
# If M<>N
# OK, so this would be for lattice paths from 0,0, to n,k
# it should equal (  n + k )  = for the binomial coefficient  =    n+k!
#                      n                                           n!(k)!
# So, it appears we just need a function to do this
# module 10^9 + 7 of course, just because that's what this asked...

import math

samples = input()
modulus = 10**9 + 7

def binomial_coefficient(n, k):
    sum = math.factorial(n+k) /(math.factorial(n) * math.factorial(k))
    return sum% modulus

for i in xrange(samples):
    (n, k) = map(int, raw_input().split())
    print binomial_coefficient(n, k)
