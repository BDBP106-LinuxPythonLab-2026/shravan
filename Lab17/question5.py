#!/usr/bin/python3
#24 sept, 2026
#question5
"""script to print the first half of a string, S."""
N=input("Enter a string: ")
half_len=len(N)//2
print (f'Half length of the string is: {half_len}')
half=N[:half_len]
print (f'Half length elements of the string are: {half}')

