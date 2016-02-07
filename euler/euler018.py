# Enter your code here. Read input from STDIN. Print output to STDOUT


# So the number of combinations is simply 2^N where N = # of lines, since
# e.g  0 = 1 solution
#   0
#  3 7   = 2 solutions, 3 or 7
#
#   0
#  3 7
# 1 4 8  = 4 solutions, 4, 7, 11, and 15
# etc.
#
# Algorithmically 
# the paths would be named e.g
# 000, 001, 011, 012
# or tree of 4:
# 0000, 0001, 0011, 0012, 0111, 0112, 0122, 0123
# ..and so forth
#
# so for the tree, say knowing there were answers
# all 8 needs node 1
# 4 needs 00, 4 needs 01
# 2 needs 000, 001, 011, 012
# 8 scans
#
# edit Feb 2016
# ok I've been going about this the wrong way, think recursion is inevitable
# say 
#   0
#  3 7
# 1 4 8
# I should make a function find max (row, col)
# so 0, 0, seek findmax(1,0) and findmax(1,1)
# findmax(1,0) checks findmax (2,0) vs findmax(2,1)
# findmax(1,1) checks findmax (2,1) vs findmax(2,2)
# findmax(2,1) would at node 1 with no children, so just returns itself



def getchildren(array, x, y):
    curval = array[x][y]
    try:
        maxleft = getchildren(array, x+1, y)
        maxright = getchildren(array, x+1, y+1)
        if maxleft > maxright:
            return curval + maxleft
        else: 
            return curval + maxright
    except:
        return curval    
    
samples = input()

for x in xrange(samples):
    lines = input()
    array2D=[]
    for i in xrange(lines):
        (values) = map(int, raw_input().split())
    print getchildren(array2D, 0, 0)
        
    
