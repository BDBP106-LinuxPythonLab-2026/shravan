#!/usr/bin/python3
#25 sep, 2026
#question8
"""Write a program to interchange the even and odd components of an input list. The list
can contain any type of variables. Output the result for the following example:
[23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]"""

input_list=[23,32,33,44,'BDBH101','hello','python',15,1e-10,True,'hit']
print('Input list is ',input_list)

interchanged_list=input_list.copy()
if len(interchanged_list)%2==0:
    end=len(interchanged_list)
else:
    end=len(interchanged_list)-1
for i in range(0,end,2):
    interchanged_list[i],interchanged_list[i+1] = interchanged_list[i+1],interchanged_list[i]

print('Interchanged list is ',interchanged_list)
