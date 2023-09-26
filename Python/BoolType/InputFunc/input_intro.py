# input function allows us to work with dynamic values.
# Because values will be given by user when the code runs.
# Input function will always give the data as text(str), so we should convert it 
# according what we need using functions like (int(), float(), bool()).

# Example of using input function
# Are we expecting int input below?


var1 = int(input('Enter your age:'))
print("The user's age is",var1) # This will print user's name
print(type(var1)) # Type will be class 'str'> text

# Print True if the older than 21, print False otherwise.

is_older = var1 > 21

print("Is user older than 21?",is_older)















