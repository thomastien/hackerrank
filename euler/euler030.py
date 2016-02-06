# Enter your code here. Read input from STDIN. Print output to STDOUT

# ok first let's think, largest N is 6, largest digit is 9, 9^6 = 531441
# 10 digit number, even smallest one 1,000,000,000 > 531441* 10
# so this is really capped at more like (9^6) * 7 = 3,720,087  (still will take too longer, but manageable...)
cap = 3720087

cap = 1000000

n = input()

def splitsum(n, i):
    array = list(map(int, str(i)))
    sum = 0
    for elem in array:
        sum = sum + elem**n
    return sum    

answer = 0
for i in xrange(2,cap):
    val = splitsum(n,i)
    #print val, ' vs ', i
    if val == i:
        answer = answer + val
        
print answer        

