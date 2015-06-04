# The header is missing and there are unnecessary imports
import random, getopt, sys, os

# This line will only work in Python 2
print "This script is not perfect, but slightly better"

# The following loop could be written in a single line with list comprehension
random_numbers = []
for i in range(10):
    random_numbers.append(random.random())

# Don't do this. Just don't.
for i in range(len(random_numbers)):
    print random_numbers[i]

# This loop could be rewritten with enumerate

for i,r in enumerate(random_numbers):
    print(i, r)

# This is not C
if(len(random_numbers)>5): 
	print("Lots of random numbers here")
