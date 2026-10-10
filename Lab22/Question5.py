#!/usr/bin/python3
#oct 04, 2026
#question5
"""Write a decorator measure_time to calculate how long a function takes to run. Use it
on a function that calculates the factorial of a number. Use a test case of calculating the
factorial of 50."""
import math
import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in s: ", func.__name__, end - begin)

    return wrapper


@calculate_time
def fact(n):
    time.sleep(3)
    print(math.factorial(n))


fact(53)