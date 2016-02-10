# Enter your code here. Read input from STDIN. Print output to STDOUT

array = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
names = []
letterscore = {}

# Assign a letter score to each alphabet
for i in xrange(len(array)):
    letterscore[array[i]] = i+1

# Get list of names, sort it
samples = input()
for i in xrange(samples):
    names.append(raw_input())
names.sort()


# Find the scores
namescores = {}
def findScore(name, position):
    decomposed = list(name)
    score = 0
    for i in decomposed:
        score = score + int(letterscore[i])
    score = score * position
    return score

for i in xrange(len(names)):
    namescores[names[i]] = findScore(names[i], i+1)

# Get list of Q/A, output the scores previously found
answers = input()
for i in xrange(answers):
    print namescores[raw_input()]
    
