#!/usr/bin/python3
#25 sep, 2026
#question6
"""Write a program with a function to calculate the area of a triangle using the formula,
where a, b, c are sides of the triangle, also providing a test case output from the program
Area=(s(s − a)(s − b)(s − c))**1/2 where 2s = a + b + c."""
def area(side_a, side_b, side_c):
        s=(side_a+side_b+side_c)/2
        #print(s)
        Area=((s*(s-side_a)*(s-side_b)*(s-side_c))**(1/2))
        a=float(Area)
        print(f'the area of the triangle is: {a}')

side_a = 12
side_b = 12
side_c = 12

area(side_a, side_b, side_c)

# s=(side_a+side_b+side_c)/2
# #print(s)
# Area=((s*(s-side_a)*(s-side_b)*(s-side_c))**(1/2))
# a=float(Area)
# print(f'the area of the triangle is: {a}')