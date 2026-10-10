#!/usr/bin/python3
#Oct 10, 2026
#Question7
"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence."""

def analyse_dna(seq):
     def gc_content(a,t,g,c):
         gc= g+c
         atgc= a+t+c+g
         percentage=(gc/atgc)*100
         print(percentage)
         return percentage
     a=0
     t=0
     c=0
     g=0
     for n in seq:
         if n=="A":
             a+=1
         elif n=="T":
             t+=1
         elif n=="G":
             g+=1
         else:
             c+=1
     gc_content(a,t,g,c)
     if g+c>a+t:
         print("more GC")
     elif g+c==a+t:
         print("equal GC & AT content")
     else:
         print("more AT")


seq=input("enter a DNA seq: " )
analyse_dna(seq)
