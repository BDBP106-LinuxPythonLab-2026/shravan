#!/usr/bin/python3
#Question8&9
"""Write a function analyse_dna(sequence) that defines an inner function gc_content()
to calculate GC% . The outer function should print whether the given DNA is AT rich
or GC rich sequence. (copy this code from Lab 21 to Lab 22 folder)"""
"""Write a decorator log_function_call that prints Running DNA analysis.... before
and Analysis complete! after any function. Apply it to the above function that returns
the GC % of a DNA sequence."""

def log_function_call(func):
    def wrapper(*args, **kwargs):
       print("Running DNA analysis....")
       func(*args, **kwargs)
       print("Analysis complete!")
    return wrapper

@log_function_call
def analyse_dna(seq):
    def gc_content(a, t, g, c):
        gc = g + c
        atgc = a + t + c + g
        percentage = (gc / atgc) * 100
        print(percentage)
        return percentage

    a = 0
    t = 0
    c = 0
    g = 0
    for n in seq:
        if n == "A":
            a += 1
        elif n == "T":
            t += 1
        elif n == "G":
            g += 1
        else:
            c += 1
    gc_content(a, t, g, c)
    if g + c > a + t:
        print("more GC")
    elif g + c == a + t:
        print("equal GC & AT content")
    else:
        print("more AT")


seq = input("enter a DNA seq: ")
analyse_dna(seq)
