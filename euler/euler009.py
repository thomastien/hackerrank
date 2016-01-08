# Enter your code here. Read input from STDIN. Print output to STDOUT

# OK, I have actually thought about this before no?
# for these to work, it's always like
# 3, 4, 5
# the nature of squares is
# 9, 16, 25, 36, 49 etc (increments 7, 9, 11, 13,)
# so distance between square N and square (n-1) is always n + (n-1), so if you find 2N-1 = square
# note it has to be an odd #, so skip 16
# 25 is next so 5, 12, 13 is another 
# 36 skip, 49 = 7, 24, 25
#
# On to wikipedia
# Euclid's formula
# for integers m, n, where m> n
# a=m**2 - n**2
# b=2mn
# c=m**2 + c**2
# would inevitably for a pythagorean triple
# so given , 12
# 3, 4, 5
# 1,3=  8, 6, 10 (3,4,5 x 2)
# 1,4=  15, 8, 17 
# 1,10= 99, 20, 101 (note this clearly exceeds upperbound already)
# 2,3=  5, 12, 13
# 3,4=  7, 24, 25
# 3,7=  40, 42, 58 (20, 21, 29)

# never mind, defaultdict is a hash of lists
# I want a list of hashes
from collections import defaultdict
debug =0
sets = defaultdict(list)
currmax = {}

# m and n are seeds
# so let's think, how would this get the set, 30,40,50?
# what mns give 20? 10:2 and 4:5
# 
for m in xrange(1,200):
    for n in xrange(1,m):
        a = m**2 - n**2
        b = 2*m*n
        c=  m**2 + n**2
        
        
        for powers in xrange(1,500):
            d = int(a * powers)
            e = int(b * powers)
            f = int(c * powers)
            total = d + e + f
                      
            
            if total <= 30000:
                if sets[total]:
                    if (d*e*f >= currmax[total]):        
                        if debug:
                            print "replacing ", sets[total], 'with',  d,e,f
                        sets[total] = [d,e,f]
                        currmax[total] = d * e * f
                    elif debug:
                        if total==120:
                            print "duplicate set found for %i" % total
                else:
                    sets[total] = [d,d,f]
                    currmax[total] = d * e * f
                    #print total, sets[total]

T = int(input())
for i in xrange(T):
    N = int(input())
    if debug:
        print "%i was N" % N
    try:
        #index = max(k for k in sets if k == N)
        #print index
        index = N
        #print sets[index]
        print currmax[index]
    except:
        print -1


