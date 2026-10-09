#!/usr/bin/python3
#25 sep, 2026
#question7
"""Write a program with a function to find whether a given triangle with sides a, b, c is
isosceles, scalene or equilateral triangle, also provide a test case output from the program."""
def triangle(a, b, c) :
      if a == b == c :
           print("It is an equilateral triangle.")
      elif a == b or a == c or b == c :
           print("It is an isosceles triangle.")
      else :
           print("It is a scalene triangle.")

triangle (1,1,1)
triangle (23,45,23)
triangle (20,23,42)