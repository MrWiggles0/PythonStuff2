from numpy import *

n = int(input("Enter the maximum power of the polynomial: "))

x = int(input("Enter the number to be solved for: "))

y = 0
print("Enter the coefficents of the polynomial in order of lowest to highest")

for i in range(n+1):
	c = int(input("Enter coefficient: "))
	y = y + c*x**i
	
print("The answer is ", y)
