# John wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# John needs to walk 10000 steps daily  OR needs to run at least
# 4 miles a day.  and Addition to these , John needs eat less 
# than 1500 calories daily. We should create a program to calculate 
# if John can loose weight or not 
# Daily steps and running distance and daily calorie intake will be given by user
# Our goal is to print True when John can lose weight and False otherwise

walk = int(input("Please enter amount of your steps:")) >= 10000
run = int(input("Please enter amount miles ran:")) >= 4
calorie = int(input("Please enter calorie intake:")) < 1500
walk_and_run = walk or run
result = walk_and_run and calorie
print(result)



















