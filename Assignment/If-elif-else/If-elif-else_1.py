# Write a Python program to get next day of a given date using if-elif-else
year = int(input("Input a year: "))

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


date = int(input("Input a date "))

if date < month_length:
    date += 1
else:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd/mm/yyyy] %d-%d-%d." % (date, month, year))
