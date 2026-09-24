#!/usr/bin/python3
#24 sept, 2026
#question14
"""program to remove all occurrences of an element from a list, L."""
w=[1,2,1,25,1,54,13,4,13,51,1,2,12,25,1]
print(w)
element=int(input("Enter an element: "))
while element in w:
        w.remove(element)
print(w) 
