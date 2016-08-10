#!/usr/bin/env python
# This program takes an input and uses it to run 
# the amout of times to calculate bits

iRange = None
		
def in_num(iRange):
	iRange = input('Enter number -->')
	if iRange >= 100:
		print "Number too high"
		check_add(iRange)
	return int (iRange)
	
def check_num(iRange):
	try:
		i = in_num(iRange)
		bit = 2
		for i in range(i):
			bit = bit + bit
			print(bit, " Bits after")
	except TypeError:
		print "Not a number"
	except NameError:
		print "Not a number"
	except KeyError:
		print "Not a number"
	
	check_num(iRange)
		
check_num(iRange)

