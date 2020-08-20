# Types of arguments
# There may be several types of arguments which can be passed at the time of function call.

# 1. Required arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Variable-length arguments

#********************************************************************************************
# Keyword arguments
#********************************************************************************************
# When we call a function with some values, these values get assigned to the arguments 
# according to their position.
# 
# Python allows functions to be called using keyword arguments. When we call functions in 
# this way, the order (position) of the arguments can be changed. 


def add(x,y):
  return x+y

# 2 keyword arguments
sum= add(x=10, y=20) 
print("sum = ",sum)

# 2 keyword arguments (out of order)
sum= add(y=20,x=10) 
print("sum = ",sum)

# 1 positional, 1 keyword argument
sum= add(10,y=10) 
print("sum = ",sum)

# Having a positional argument after keyword arguments will result in errors. 
# sum= add(x=20,10) 
# print("sum = ",sum)

#syntaxError: positional argument follows keyword argument


#doesn't find the exact match of the name of the arguments (keywords)
# sum= add(a=10, b=20) 
# print("sum = ",sum)

# TypeError: add() got an unexpected keyword argument 'a'


