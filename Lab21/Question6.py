#!/usr/bin/python3
#Oct 10, 2026
#Question6
"""Write a function called cell_metabolism that takes the number of glucose and oxy-
gen molcules, that contains an inner function energy_output() to calculate ATP yield
(assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
produced."""

def cell_metabolism(O,G):
    def energy_output(a):
            Atp = 38 * a
            print(Atp)
    if O == 6 * G:
        energy_output(G)
    elif G > O / 6:
        energy_output(O / 6)
    else:
        energy_output(G)




cell_metabolism(1,6)
