# Ask users to enter 2 equal integer variables,
# If user enters 2 equal numbers, we will print `You entered 2 equal numbers.`
# If user enters 2 different numbers, we will print `You didm't follow the instructions.`

print("Enter two numbers below that are equal")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if num1 == num2:
    print("You entered two equal numbers.")
elif num1 != num2:
    print("You didn't follow the instructions.")

# Note! By using elif statement we are telling python that both conditions can't
# be True, so if the first condition is True it doesn't check the elif condition.
# We could say that we use elif statement for conditions that depend on each other
# so either one or the other is True.











