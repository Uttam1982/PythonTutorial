# What is if...else statement in Python?

# Decision making is required when we want to execute a code only 
# if a certain condition is satisfied.

# The if…elif…else statement is used in Python for decision making.


# ******************************************************************************
# Python if Statement Syntax
# ******************************************************************************
# Will execute statement(s) only if the test expression is True.
# If the test expression is False, the statement(s) is not executed.


# Example: Python if Statement

num = 5
if num > 0:
  print(num, "is a postive number")
print("This will always be printed")

num = -1
if num > 0:
  print(num, "is a postive number")
print("This will always be printed")


# ******************************************************************************
# Python if...else Statement
# ******************************************************************************
# If the condition is False, the body of else is executed. 
# Indentation is used to separate the blocks.

# Example of if...else

#num = 5
#num = -1
num = 0
if num >= 0:
  print("Positive or zero")
else:
  print("Negative number") 


# ******************************************************************************
# Python if...elif...else Statement
# ******************************************************************************
# The elif is short for else if. It allows us to check for multiple expressions.
# If the condition for if is False, it checks the condition of the next elif block and so on.
# If all the conditions are False, the body of else is executed.
# The if block can have only one else block. But it can have multiple elif blocks.

# Example of if...elif...else

'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = 5
# num = 0
# num = -1

if num > 0:
  print("positive number")
elif num == 0:
  print("Zero")
else:
  print("Negaive number")


# ******************************************************************************
# Python Nested if statements
# ******************************************************************************
# We can have a if...elif...else statement inside another if...elif...else statement. 
# This is called nesting in computer programming.

'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number : "))

if num >= 0:
  if num == 0:
    print("zero")
  else:
    print("Positive number")
else:
  print("Negative number")
