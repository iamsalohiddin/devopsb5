# Logical operators in pyhton

## *and* operator
- `and` operator checks if **all** conditions are True. For ex:
```py
# Let's write a program to see if a person can drive:
# In order to drive the must be over 15 years old and they must have a valid driver's license.
age = 18
has_license = True
can_drive = has_license and age > 15
```

## *or* operator
- `or` operator checks if at least one condition is True. For ex:
```py
# A worker can get rest when it is weekend or when it is on holidays.
is_holiday = True
is_weekend = False
can_rest = is_holiday or is_weekend
```
## *not* operator
- Reverses the result of a boolean variable. For ex:
```py
b1 = True
b1 = not b1
print(b1) # False
b1 = not b1
print(b1) # True
```
# Notes:
```py
print(True and not False) # True
print(not True and True) # False
print(True and True and True and False) # False
print(True or False) # True
print(not False or False) # True
print(False or False) # False
print(False and False) # False

# Using both `and` and `or` operator at the same time.
# In python `and` operator will be executed before the `or` operator.
print(False or True and False) # False
# Note! `not` operator will be executed before the `and` and `or` operators.
```

# Immutable 
- All numerical data types in python are immutable which means their value will not be modified in any case other than reassignment.
# Escape character in str
- If you want to add unallowed character to the string you can use backslash \ to insert those unallowed characters.
```py
# In python we can't use " if the text is defined in ' "
# print(" \" ") # This will print " only
print('\'') # This will print ' only
```

# Note!
- Any bool variable that is used in arithmetic operation will take the value 1 or 0, depending on it is True or False.





















