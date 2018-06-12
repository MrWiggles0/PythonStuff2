#Jonathan Doucette
#ME492
#Week 3 Day 4 Assignment 2

hrs = int(input("Enter the number of hours worked: "))
rate = int(input("Enter the rate of pay: "))

if hrs <= 40:
	payment = hrs*rate
else:
	payment = (hrs-40)*(1.5*rate) + 40*rate

print "Pay the employee $", payment
