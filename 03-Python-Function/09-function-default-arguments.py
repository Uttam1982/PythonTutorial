# Types of arguments
# There may be several types of arguments which can be passed at the time of function call.

# 1. Required arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Variable-length arguments

#********************************************************************************************
# Default arguments
#********************************************************************************************
# Function arguments can have default values in Python.
# We can provide a default value to an argument by using the assignment operator (=). 


def add(x,y=2):
  return x+y

sum= add(1) 
print("sum = ",sum)

sum= add(1,5) 
print("sum = ",sum)

# TypeError: add() missing 1 required positional argument: 'x'
# sum = add()  
# print("sum = ",sum)

#Explanation
# 1. In this function, the parameter x does not have a default value 
#    and is required (mandatory) during a call.

# 2. The parameter y has a default value of 2. So, it is optional during a call. 
#    If a value is provided, it will overwrite the default value.

# 3. Any number of arguments in a function can have a default value. 
#    But once we have a default argument, all the arguments to its right must also have 
#    default values

# 4. This means to say, non-default arguments cannot follow default arguments.

# def add(x = 2,y):
#   return x+y

# SyntaxError: non-default argument follows default argument