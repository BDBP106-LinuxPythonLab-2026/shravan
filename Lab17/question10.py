#!/usr/bin/python3
#24 sept, 2026
#question10
"""program to find the even numbers in a list, L."""
L = [1,2,3,4,5,5,7,8,9,10,11,12]
even_numbers=0
for num in L:
     if num % 2 == 0:
         print(f'{num}')
         even_numbers=even_numbers+1
print(f'Total Even numbers in the list are : {even_numbers}')

