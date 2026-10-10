#!/usr/bin/python3
#Oct 09, 2026
#Question4
"""Write a program to filter out the odd elements of the Fibonacci series for the first n
terms."""

n=15
a=0
b=1
listt=[0,1]
for i in range(2,n):
    i=a+b
    a=b
    b=i
    listt.append(i)
print("fib seies",listt)

filtered=list(filter(lambda a: a % 2 , listt))
print("filtered fib. list:",filtered)
