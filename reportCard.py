from numpy import *

cla = int(input("How many classes did you take? "))

name = []
grade = []

gra = 0.0
for i in range(cla):
	na = raw_input("Class name: ")
	name.append(na)
	g = int(input("Grade: "))
	grade.append(g)
	gra = gra + grade[i]

gpa = gra/cla
print("*********************")
print("REPORT CARD:")
for i in range(cla):
	print name[i], " - ", grade[i] 

print "Overall GPA - ", gpa
