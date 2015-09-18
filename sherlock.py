#!/usr/bin/python

cases = input()
count = 0;
while (count < cases):
    count+=1
    digit = input()
    #print "processing %s" % digit
    remaining = digit
    next_flag = 0
    while (remaining%3 <> 0):
        if remaining < 3:
            next_flag = 1;
            print -1;
            break;
        remaining -= 5
    
    #print 'reached'
    if (next_flag <> 1):
        num_3s = digit - remaining
        num_5s = remaining
        print '5'*num_5s + '3'*num_3s
    
