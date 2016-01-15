# Enter your code here. Read input from STDIN. Print output to STDOUT

# Too easy for an euler problem, simple 2-D array...

arr = []
for arr_i in xrange(20):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
maxsum = 0
value = 0
for x in xrange(20):
    for y in xrange(20):
            # hori
            if x < 17:
                value = arr[x][y] * arr[x+1][y] * arr[x+2][y] * arr[x+3][y]
                if value > maxsum:
                    maxsum = value
                # right \ diagonal
                if y < 17:
                    value = arr[x][y] * arr[x+1][y+1] * arr[x+2][y+2] *arr[x+3][y+3]
                    if value > maxsum:
                        maxsum = value
            # verti
            if y<17 :
                value = arr[x][y] * arr[x][y+1] * arr[x][y+2] * arr[x][y+3]
                if value > maxsum:
                    maxsum = value
          
            # left / diagonal   
                if x > 2 :
                    value = arr[x][y] * arr[x-1][y+1] * arr[x-2][y+2] * arr[x-3][y+3]
                    if value > maxsum:
                        maxsum = value
                

print maxsum
