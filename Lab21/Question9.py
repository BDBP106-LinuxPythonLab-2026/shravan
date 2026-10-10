#!/usr/bin/python3
#Oct 10, 2026
#Question9
"""Write a function population_growth(initial,rate, time) that defines an inner func-
tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0

represents the initial population and N(t) is population after time t. The inner function
returns the population after time, and the outer function rounds and prints it."""

import math

def population_growth(initial,rate, time):
    def exponential_growth():
        pp = initial + math.exp(rate * time)
        print(pp)
        return pp
    P= exponential_growth()
    print(round(P))


population_growth(2467848,3,24)