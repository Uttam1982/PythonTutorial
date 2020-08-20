# Types of arguments
# There may be several types of arguments which can be passed at the time of function call.

# 1. Required arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Variable-length arguments

#********************************************************************************************
# Required arguments
#********************************************************************************************
# These are the arguments which are required to be passed at the time of function calling 
# with the exact match of their positions in the function call and function definition. 
# If either of the arguments is not provided in the function call, or the position of the 
# arguments is changed, the Python interpreter will show the error.


def add(x,y):
  return x+y

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

sum= add(n1,n2) 
print("sum of {} and {} is {}".format(n1,n2,sum))

# TypeError: add() missing 1 required positional argument: 'y'
#sum = add(n1)  
#print("sum of {} and {} is {}".format(n1,n2,sum))

