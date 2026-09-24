#!/usr/bin/python3
#24 sept, 2026
#question3
"""script to check if a given number, N, is prime or not"""
N=int(input("Enter a number: "))
if N <= 1:
    print(f"{N} is not a prime number.")
else:
    for i in range(2, N):
        if N%i==0:
            print(f"{N} is not a prime number.")
            break
    else:
        print(f"{N} is a prime number.")

