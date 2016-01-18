# Enter your code here. Read input from STDIN. Print output to STDOUT



# 1 2 4 8 16 32 64 128 256 512 1024 2048 | 4096 8192 16384 32768 65536 131072
# 1 2 4 8 7 5 1 2 4 8 7 5 |  1 2 4 8 7 5
# ok I see a pattern, it always maps to 1 2 4 8 7 5
# based on the mod 6
# EDIT: No that's not what they want either, sigh...only single addition
# so 1 2 4 8 7 5 10 11 13 8 7 14 19 20 22 26 25 14...etc

import math
#mapping = [1, 2, 4, 8, 7, 5]

# not used, misunderstood question thought could shortcut this
def find_answer(value):
    modifier = value%6
    return mapping[modifier]

def find_answer_old(value):
    # Using float is going to overflow for the test case 100,000
    #answer = int(math.pow(2, value))
    # stick with int
    answer = int(2**value)
    
    answer = list(str(answer))
    answer = map(int, answer)
    return sum(answer)

samples = input()

for i in xrange(samples):
    value = input()
    print find_answer_old(value)
    
