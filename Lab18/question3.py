#!/usr/bin/python3
#25 sep, 2026
#question3
"""a program to find the maximum and minimum values of a dictionary."""
D = {'apple': 5,'banana': 3,'orange': 0,'grape': 5}
max = max(D, key=D.get)
min = min(D, key=D.get)
print(f"Maximum: '{max}' with a value of {D[max]}")
print(f"Minimum: '{min}' with a value of {D[min]}")
