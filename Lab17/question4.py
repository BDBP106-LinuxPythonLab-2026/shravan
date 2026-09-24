#!/usr/bin/python3
#24 sept, 2026
#question4
"""a script to print individual digits of a number, N."""
N=int(input("Enter a number: "))
a=1
for digit in str(N):
      print (f'digit{a}: {digit}')
      a+=1
