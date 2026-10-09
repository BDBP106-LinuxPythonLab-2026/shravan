#!/usr/bin/python3
#25 sep, 2026
#question2
"""a program to sum all the values of a dictionary."""
D = {'apple': 50,'grapes': 30,'orange': 25}

total = 0
for value in D.values():
    total += value

print(f"The total sum of values is: {total}")
