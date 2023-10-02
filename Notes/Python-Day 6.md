# If Statent in Python
- Purpose of an `if` statement is executing the certain parts of the code depending on given `bool` conditions.
- When a `bool` condition is True for the `if` statement the **next** block of code will be executed.

#### How do we know where next block of code starts and ends?
- In python, same block of codes has same indentation. So that, by looking at the indentation, we could understand beginning and end of the block of codes.
**Note!** A block of code refers to the lines of codes that belong to same implementations. This implementations could be `if` statement, methods, class etc.

#### How `if` statement works?
```py
if boolean_cond:
    # code belongs to if
    # code belongs to if
# code that is not affected by if statement, this line will always get executed regardless of the if statement's condition.

```
**Note:** As seen on the example above, only if a bool condition is True, if block will get executed.

## Examples:
```py
if True:
    # Line1
    # Line2
# Line3

# Which of the lines will be executed?
# Since the condition is True, code block of if statement(Line1 and Line2) will get executed. Line3 will never be affected by if statemen so it will always get executed
```

```py
if False:
    # Line1
    # Line2
# Line3
# Which of the lines will be executed?
# Since the condition is False, code block of if statement(Line1 and Line2) will NOT get executed. Line3 will never be affected by if statemen so it will always get executed
```












