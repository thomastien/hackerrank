#!/usr/bin/python

cases = input()


# Strategy: rather than doing a hard count
# Mathematically, it seems I can just do this by
#	Counting all the multiples of 3, so if 20
#		there're 6 of them, with 6=N with sum expected to be 3 X ((N^2)+N) / 2
#		So, 10 = 18 
#		   100 = 33^2+33/2   * 3 = 1683
#	Counting all the multiples of 5, so if 20
#		there're 4 of them, same gives 30
#		100 = 20 of them, 1050 (20^2+20)/2  * 5 = 1050
#	So for 100, it was 1683+1050 = 2733
#	BUT the multiple of 15 are DOUBLE-counted
#		100 = 6 of them, 21*15 = 315 
#	2733-315 =  2418 
# (This is for problem parameter T=101, if T=100 T itself should be excluded = 2318  

def mults_3(number):
	n = number/3
	return ((n**2 + n)/2) * 3

def mults_5(number):
	n = number/5
	return ((n**2 + n)/2) * 5

def mults_15(number):
	n = number/15
	return ((n**2 + n)/2) * 15

debug = 0


for i in range(1,cases+1):
	sample = input()-1
	
        if debug == 1:
		print mults_3(sample)
		print mults_5(sample)
		print mults_15(sample)
		print '------'
	print mults_3(sample) + mults_5(sample) - mults_15(sample)
