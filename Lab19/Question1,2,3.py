# #!/usr/bin/python3
# #Question1(i)
"""Create a list spanning 1 to 50 using list comprehension method. Call this list a."""

a=list(range(1,51))
print(a)

# #(ii) Slicing with positive step:
# print(" Slicing with positive step:")
# print(a[1:5])
# print(a[3:20:2])
# print(a[::2])
# print(a[::])
# print(a[10::2])
# print(a[1:1:1])
# print(a[:0:])
# print(a[-7::1])
# print(a[-6:])
# print(a[-10:-4])
#
#
#
# #(iii) Slicing with negative step:
# print("Slicing with negative step:")
# print(a[::-1])
# print(a[::-3])
# print(a[:1:-2])
# print(a[-1:-1:-1])
# print(a[:-5:-1])
# print(a[:0:-1])
# print(a[:-1:-1])
# print(a[0:-5:-1])
# print(a[-1:5:-1])
# print(a[2:2:-1])
# print(a[2:1:-1])
# print(a[0:-5])

#Question(iv)
"""(iv) Modification of lists using list slicing:
(a) Create a list of even numbers from a using list slicing technique.
(b) Create a new list from a by choosing the first 10 numbers, then the even
numbers from 35-50."""
#(a)
# A=[]
# for i in range(0,50,2):
#     A.append(i)
# print(A)
# #(b)
# print(a[:10])
# print(a[35:50:2])
#
"""(2) Lists and do loops
(i) Using a simple do loop structure or list comprehension, find the sum of elements
in the above list a."""
B=sum([i for i in a])
print(B)
"""(ii) Define another list b (using list comprehension again!) containing prime numbers
from 1 to 50."""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
b = [i for i in range(50) if is_prime(i)]
print(b)

"""(iii) Using a do loop structure, collect all the common numbers in a and b into a new
list c."""
c=[j for i in a for j in b if i==j]
print(c)


"""(3) List comprehension with strings Use list comprehension technique you learnt in class
to do the following
(i) Using the join method.
(a) Create a string by joining the numbers in the above list a using the comma.
(b) Create a string by joining the numbers in the above list a using the period.
(c) Create a string by joining the numbers in the above list a using the ‘—’.
(d) Create a new string by first creating a list of squares of the elements in a,
then listing them alongside the elements of a line by line. In other words,
we want a data set that looks like
1 1
2 4
3 9  """

#(a)
A="".join(str(i) for i in a)
print(A)
B=",".join( i for i in A)
print(B)
C="-".join( i for i in B)
print(C)
sq=[i*i for i in a]
d="\n".join([" ".join([str(a[i]),str(sq[i])]) for i in range(0,len(a))])
print(d)

"""(ii) Make a list of 10 people you know, and do the following:
(a) Convert each element in the list to upper case using list comprehension
(b) Swap the first name and surname of each element in the list
(c) Join the first name and surname in each element as ’First.Last’. Note that
the first letter of the first name and first letter of the surname should be
upper case."""

people=["abhi tiwari", "chikka siddu", "mahima shukla","sugee Godehera", "divya b", "Sanjana Pillai", "akash yadav", "rohit sharam", "virat kolhi", "M S Dhoni"]
case=[i.upper() for i in people]
print(case)
peopless=peopless = [" ".join(name.split()[::-1]) for name in people]
print(peopless)
peoplesss=[".".join(name.title().split()[::1]) for name in people]
print(peoplesss)

"""(iii) Find the longest word in this sentence using list comprehension: ”She sells sea
shells that she collects from the sea floor”."""

scen="She sells sea shells that she collects from the sea floor"
longestword = [max([word for word in scen.split()], key=len)]
print("The longest word is :"+str(longestword))

"""Create a list of the words that are repeated in the above sentence."""
rw=[scen.split()[i] for i in range(0,len(scen.split())) for j in range((i+1),len(scen.split())) if scen.split()[i]==scen.split()[j]]
print("The repeated words are: "+str(rw))