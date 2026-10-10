#!/usr/bin/python3
#Oct 09, 2026
#Question3
"""Write a program to convert a tuple of angles into a list of tuples with each tuple containing
the sine and cosine of an angle"""
import math
Angles=(23,23,45)
sincosin=list(map(lambda a : (math.sin(a),math.cos(a)) , Angles))
print(sincosin)