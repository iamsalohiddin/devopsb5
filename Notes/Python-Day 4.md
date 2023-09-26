
# Python Comparison Operators

### 1. Equal to **==**
- Checks if the value on the left is equal to the value on the right.
**Example**
```py
print(11==11)
```
**Output**:
#### Note! Comparison operators always result in a boolean value.
- For the code above, since the 11 is the same as 11 the output of the code will be 'True'.

### 2. Not Equal to **!=**
- Checks if the left side is **not equal to** right side
```py
print(6 !='6')  # Since text can not be equal to numbers, this line will print True
print(6 != 6)   # Simce both sides of the equation is same, this will print Flase
```
### 3. Greater Sign **>**
- Checks if the left side of the equation is bigger than the left side.
```py
print(5.0 > 5)  # False 
print(3 > 4)    # False
print(10 > 9)   # True
```

### 4. Less than Sign **<**
- Checks if the left side of the equation is smaller than the left side.
```py
print(5.0 < 5)  # False 
print(3 < 4)    # True
print(10 < 9)   # False
```
### 5. Less than equal **<=** || Greater equal Sign **>=**
- Checks if the left side is smaller OR equal **<=**,
- Checks if the left side is bigger OR equal **>=**.
```py
print(5.0 <= 5)  # True
print(5.0 >= 5)  # True 
print(3 <= 4)    # True
print(10 >= 9)   # True
```

## Note! 
- **Type Matters:**
- When comparing values, type of the values is also important:
For ex: `5 == '5'` is `False` because one is str(text) and the other is int type.

- **We can chain the comparison operators in Python**

```py
print(1 < 2 < 3) # True
```

## Note! 
- `True` numerically equals to `1` and `False` numerically equals to `0`. For example:
```py
print(int(True)) # 1
print(int(False)) # 0
# When using comparison operators between boolean and int type, python auto converts bool type into int.
print(True == 1)    # True
print(True > False) # True
print(False < 3)    # True
```
## Converting other types to bool 
- Which function do you think we are going to use to convert other types to boolean?
**bool()** function.
```py
b = bool(-2)
print(b) # True
b1 = bool(0)
print(b1) # False
```
#### every number except `0` will result in `True`.





















