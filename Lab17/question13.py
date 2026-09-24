#!/usr/bin/python3
#24 sept, 2026
#question13
"""a program to extract elements of a list, if it occurs more than k times."""
w=[1,2,1,25,1,54,13,4,13,51,1,2,12,25,1]
k=2
extract=[]
for i in w:
    if w.count(i) == k:
        extract.append(i)
print(extract) 

