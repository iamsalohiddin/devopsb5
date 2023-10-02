quarter = int(input("Enter the amount of Quarters:"))
dimes = int(input("Enter the amount of Dimes:")) 
nickels = int(input("Enter the amount of Nickels:")) 
pennies = int(input("Enter the amount of Pennies:")) 

quarter_in_dollars = quarter*25
dimes_in_dollars = dimes*10
nickles_in_dollars = nickels*5
pennies_in_dollars = pennies*1

total = (quarter_in_dollars+dimes_in_dollars+
         nickles_in_dollars+pennies_in_dollars)/100

print("The total in dollars is $", total)







