var1 = int(input("Please enter 5-digit number:"))

five_digit = var1
four_digit = var1//10
three_digit = four_digit//10
two_digit = three_digit//10
one_digit = two_digit//10

fifth = one_digit
forth = two_digit%10
third = three_digit%10
second = four_digit%10
first = five_digit%10

print(first,second,third,forth,fifth)













