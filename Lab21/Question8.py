#!/usr/bin/python3
#Oct 10, 2026
#Question8
"""Write a function protein_energy_temp() with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0)."""

def protein_energy_temp(H,T,S):
    # H=H
    # T=T
    # S=S
    def calculate_free_energy(H,T,S):
        G = H - (T * S)
        print(G)
        return G

    A= calculate_free_energy(H, T, S)
    if A < 0:
        print("""stable""")
    else:
        print("unstable")


A=int(input("enter H: "))
B=int(input("enter T in kelvin: "))
C=int(input("enter S: "))
protein_energy_temp(A,B,C)



