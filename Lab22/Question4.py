#!/usr/bin/python3
#Oct 10, 2026
#question2
"""Write a decorator called check_positive that checks whether the argument passed to
a function is positive. If it is positive, execute the function; otherwise, print
"Number must be positive"."""
def check_positive(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            print("Number must be positive")
    return wrapper


@check_positive
def process_number(n):
    print(f"The number {n} is positive!")


#Testing the decorator
num = int(input("Enter a number: "))
process_number(num)