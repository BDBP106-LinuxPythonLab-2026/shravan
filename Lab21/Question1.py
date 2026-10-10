#!/usr/bin/python3
#Oct 09, 2026
#Question1
"""Write a program to convert temperature in Celsius to Fahrenheit using map function."""
#Celsius to Fahrenheit=(celsius*1.8)+32

temperature=[35,0,34,]
far=list(map(lambda c:((c*1.8)+32),temperature))
print(far)