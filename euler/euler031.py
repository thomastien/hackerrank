# Enter your code here. Read input from STDIN. Print output to STDOUT

coins = [1,2,5,10,20,50,100,200]
T = input()
debug =False
modulus = 10**9 + 7
n_values = []


max = 0

# Find the max, so we only have to populate ways[] once
for i in xrange(T):
    N = input()
    n_values.append(N)
    if N > max:
        max = N

ways = [1] + [0]*max
for coin in coins:
    for i in range(coin, max+1):
        ways[i] += ways[i-coin]


# iterate through the N values and give the answer from N
for i in (n_values):
    answer = ways[i] % modulus
    print answer

    
    
    
