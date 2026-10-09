#!/urs/bin/python3
#26 sep, 2026
#question11
"""A magic date is a date where the date multiplied by the month is equal to the two-digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60 which is the two-digit year. Write a function that determines whether
or not a date is a magic date. Use your function to create a main program that finds
and displays all of the magic dates in the 20th century."""

def check_magic_date(input_date):
   #input_date is a list of day,month,year
   year = input_date[2]%100
   day = input_date[0]
   month = input_date[1]
   check_magic=False
   if day*month == year:
       check_magic=True
   return check_magic

#input_date=input('Enter a date in the format dd mm yyyy: ').strip().split()
input_date=[10,6,1960]
check_magic=check_magic_date(input_date)
if check_magic:
   print(input_date[0],'-',input_date[1],'-',input_date[2],' is a magic date.')

for yr in range(1900,2000):
    for mth in range(1,13):
        for day in range(1,32):
            if check_magic_date([day,mth,yr]):
               print('Magic date!',day,'-',mth,'-',yr)