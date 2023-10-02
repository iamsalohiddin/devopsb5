# Create a program that calculates the grade letter of student.
# Ask user their grade as an integer number.
# Print `Not a valid grade` if the grade is lower than 0 and bigger than 100
# Print A+ if grade is higher than 95.
# Print A if grade is in between 85and 94 inclusive.
# Print B if grade is in between 75 and 84 inclusive.
# Print C if the grade is in between 65 and 74 inclusive.
# Print `Grade doesn't meet expectations` when the grade is lower than 65.

var1 = int(input("Please enter your grade as an integer:"))

if 95<=var1<=100:
    print("A+")
elif 85<=var1<=94:
    print("A")
elif 75<=var1<=84:
    print("B")
elif 65<=var1<=74:
    print("C")
elif var1<65:
    print("Grade doesn't meet expectations.")
else:
    print("Not a valid grade.")

# `else` is not preffered to use unless you are 100% sure that there
# are no conditions left. Other than that, elif is always more prefferable than
# else.










