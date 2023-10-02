#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.





var1 = int(input("Please enter the year:"))
is_divisible_4 = var1 % 4 == 0
is_divisible_400 = var1 % 400 == 0
leap_year = is_divisible_4 or is_divisible_400
is_not_divisible_100 = not leap_year % 100 == 0
result = leap_year and is_not_divisible_100
print(result)

# year = int(input("enter the year that you want to learn if it is a leap year:"))
# What conditions should this year give me so that I know it is a leap year/ 
# I am looking a for a year number that is divisible by 4 but not 100. 
# Or it could be divisible by only 400 and and it is a leap year. 
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# print( "Is the given year leap? ", is_leap)












