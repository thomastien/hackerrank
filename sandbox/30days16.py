# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
import pprint


samples = input()

array = raw_input().split()
array = [int(x) for x in array]
min = 9999999
sets = defaultdict(list)

array.sort()

for i in xrange(len(array)-1):
    j = i+1
    difference = array[j] - array[i]
    val = abs(difference)
    if val <= min:
        min = val
        # This has some extra junk, but we're trying to keep sets small"er" not minimum
        if array[j] > array[i]:
            sets[val].append([array[i], array[j]])
        else:
            sets[val].append([array[j], array[i]])
#pprint.pprint(sets)
sets[min].sort()
#print sets[min]
for i in sets[min]:
    print " ".join(str(x) for x in i),
