#!/usr/bin/python3
#Oct 09, 2026
#Question2
"""Write the above program using lambda expression."""

temperature=[35,0,34,]
far=list(map(lambda c:((c*1.8)+32),temperature))
print(far)