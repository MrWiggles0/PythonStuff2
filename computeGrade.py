from numpy import *

x = float(input("Enter a number between 0.0 and 1.0: "))

while x < 0.0 or x > 1.0:
	print "Improper value"
	x = float(input("Enter a number between 0.0 and 1.0: "))

if x >= 0.9:
	print "That's an A"
elif x >= 0.8:
	print "That's a B"
elif x >= 0.7:
	print "That's a C"
elif x >= 0.6:
	print "That's a D"
else:
	print "That's an F"


