dollar = float(input("Please enter your balance:"))
balance = int(dollar * 100)
quarters = balance//25
dimes_amount = balance - 25*quarters
dimes = dimes_amount//10
nickles_amount = dimes_amount - 10*dimes
nickles = nickles_amount//5
pennies_amount = nickles_amount - 5*nickles
pennies = pennies_amount//1

print("$",balance,"will make",quarters,"quarters,",dimes,"dimes,",nickles,"nickles,",pennies,"pennies.")









