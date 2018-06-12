from numpy import *

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

xodd = True
yodd = True
zodd = True

if x%2 == 0:
	xodd = False
if y%2 == 0:
	yodd = False
if z%2 == 0:
	zodd = False

if xodd & yodd & zodd:
	if (x > y) & (x > z):
		print "x is the highest odd number"
		print x
	elif (y > x) & (y > z):
		print "y is the highest odd number"
		print y
	elif (z > x) & (z > y):
		print "z is the highest odd number"
		print z
elif xodd & yodd & ~zodd:
	if x > y:
		print "x is the highest odd number"
		print x
	else:
		print "y is the highest odd number"
		print y
elif xodd & zodd & ~yodd:
	if x > z:
		print "x is the highest odd number"
		print x
	else:
		print "z is the highest odd number"
		print z
elif yodd & zodd & ~xodd:
	if y > z:
		print "y is the highest odd number"
		print y
	else:
		print "z is the highest odd number"
		print z
elif xodd & ~yodd & ~zodd:
	print "x is the only odd number"
	print x
elif yodd & ~xodd & ~zodd:
	print "y is the only odd number"
	print y
elif zodd & ~xodd & ~yodd:
	print "z is the only odd number"
	print z
elif ~xodd & ~yodd & ~zodd:
	print "No odd numbers."
