# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
from math import sqrt

c=50
h=30
s=input("enter a coma seperated sequence:").split(',')
d=[int(i) for i in s]
q=[round(sqrt((2*c*i)/h)) for i in d]
s=[str(i) for i in q]
print(','.join(s))

# print(",".join(str(q)))
