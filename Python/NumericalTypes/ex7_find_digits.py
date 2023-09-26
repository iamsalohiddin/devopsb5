

# Create a program that will find each digit just using the variable name
# One fact is that number is always going to be 4 digit

# 32 % 10 -> 2
# 49 % 10 -> 9
# 101 % 10 -> 1
# 217 % 10 -> 7
# 8 % 10 -> 8
# 93 % 10 -> 3

# NOTE: Every time finding a remainder with 10, gives us last digit from the number

# 32 // 10 -> 3
# 496 // 10 -> 49
# 101 // 10 -> 10
# 217 // 10 -> 21
# 8 // 10 -> 0
# 93 // 10 -> 9

#NOTE: Every time the number is divided by 10 will lose its last digit.

four_digit_num = 1987
three_digit_num = four_digit_num//10
two_digit_num = three_digit_num//10
one_digit_number = two_digit_num//10

divident = 10

first_digit = one_digit_number%divident
second_digit = two_digit_num%divident
third_digit = three_digit_num%divident
fourth_digit = four_digit_num%divident

print('First digit is',first_digit)
print('Second digit is',second_digit)
print('Third digit is',third_digit)
print('Fourth digit is',fourth_digit)


















