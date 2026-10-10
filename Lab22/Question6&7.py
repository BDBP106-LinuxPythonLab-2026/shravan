#!/usr/bin/python3
#oct 04, 2026
#question6
"""Write a function population_growth(initial,rate, time) that defines an inner func-
tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
represents the initial population and N(t) is population after time t. The inner function
returns the population after time, and the outer function rounds and prints it (already
done in Lab 21, copy code to Lab22 folder)."""
"""Use the decorator measure_time to calculate how long the above function calculating
population growth that loops 1 million iterations."""
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
def population_growth(initial,rate, time):
    def exponential_growth():
        pp = initial + math.exp(rate * time)
        print(pp)
        return pp
    P= exponential_growth()
    print(round(P))


population_growth(2467848,3,24)