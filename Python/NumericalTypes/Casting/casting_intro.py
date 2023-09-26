
# In python we can also convert data types to each other using constructor
# function of that specific type.

var1 = 5.1
print(type(var1)) #<class 'float'>

var1 = 5
print(type(var1)) #<class 'int'>

var1 = "h"
print(type(var1)) #<class 'str'>

var1 = True
print(type(var1)) #<class 'boot'>

var1 = 5.1
print(type(var1)) #<class 'float'>

var1 = int(var1)
print(type(var1)) #<class 'int'>

var1 = float(var1)
print(type(var1)) #<class 'float'>

var1 = 5.9
print(var1) # 5.9
var1 = int(var1)
print(type(var1)) # <class 'int'>
print(var1) #5
var1 = float(var1)
print(type(var1)) #<class 'float'>
print(var1) #5.0

# incompatible type example

#s='techtorial'

#s=int(s)

s='6'

print(type(s))

s = int(s)
print(type(s))


















