#!/usr/bin/python3
#Oct 09, 2026
#Question5
from functools import reduce
"""Write a program to find the sum of all the elements in a list using lambda and reduce
functions."""

orig=[1,34,23,0,0,34,2,4,54,6,4,4,5,3,3,5,64,3,4,3,54,3]
summ = reduce(lambda a, b: a + b, orig)
print(summ)