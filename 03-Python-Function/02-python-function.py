# Example of a function
def greet(name):
  '''
  This function greet to
  the person passes as a 
  parameter
  '''
  print('Hello, '+name+' ! Good Morning')

#How to call a function in python?
greet('Uttam')


# The first string after the function header is called the docstring 
# and is short for documentation string. It is briefly used to explain 
# what a function does.

# #Docstrings
print(greet.__doc__)

# The return statement
# The return statement is used to exit a function and go back to the place 
# from where it was called.

print('Return value of greet function: ',greet('uttam'))
# Here, None is the returned value since greet() directly prints the name and 
# no return statement is used.

#Example of return
def absolute_value(num):
  if num >= 0:
    return num
  else:
    return -num

print('The absolute value of  4: ',absolute_value(4))
print('The absolute value of -5: ',absolute_value(-5))



