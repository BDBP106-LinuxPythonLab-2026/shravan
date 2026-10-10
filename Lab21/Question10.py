#!/usr/bin/python3
#Oct 10, 2026
#Question10
"""Write a program to extract all vowels in a given string using list comprehension."""
s=str(input("enter a string to get vowels: "))
vo="aeiou"
result="".join(i for i in s for j in vo if i==j )
print(result)