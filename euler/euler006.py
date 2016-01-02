# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()

def sumSquares(n):
    #       squares, 1, 4, 9, 16, 25, 36 etc
    # sum of squares 1  5  14  30  55  91 etc
    # formula is n(n+1)(2n+1) / 6
    return (n * (n+1) * (2*n+1)) / 6
    

def squareSums(n):
    #  sums of 1 2 3 4 5 6 7 8 9 10
    #          1 3 6 10 15 21 28 36 45 55
    # (n)(n+1)/2
    return (n * (n+1) / 2)**2

for i in range (1, t+1):
    n = input()
    #print sumSquares(n)
    #print squareSums(n)
    print squareSums(n) - sumSquares(n)
    
    
    
