#!/usr/bin/python3
#24 sept, 2026
#question11
"""Write a program to print the duplicate elements in a list, L."""
w=[1,2,1,25,1,54,13,4,13,51,1,2,12,25,1]
duplicate=[]
for i in w:
    if w.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print(duplicate) 
