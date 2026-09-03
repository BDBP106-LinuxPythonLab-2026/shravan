#Lab15
# sept 3, 2026
import math

a= input("real number a: ")
b= input("real number b: ")
c= input("real number c: ")
a=float(a)
b=float(b)
c=float(c)
x= b**2 - 4*a*c
root1 = (-b + math.sqrt(x))/(2*a)
root2 = (-b - math.sqrt(x))/(2*a)

print(root1,root2)