#!/usr/bin/python3
#25 sep, 2026
#question9
"""Write a function called nextPrime that finds and returns the first prime number larger
than some integer, n. The value of n will be passed to the function as its only parameter.
The main program should read an integer from the user and display the first prime
number larger than the entered value."""
def nextPrime(n):
  num = n + 1

  while True:
    factors= 0

    for i in range(2, num):
      if num%i==0:
        factors=factors+1
    if factors == 0:
      return num

    num+=1


number=int(input('Enter a number: '))
result=nextPrime(number)
print(f'The first prime number larger than {number} is: {result}')

