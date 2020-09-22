#---------------------------------------------------------------------------------------
# Creating Custom Exceptions
#---------------------------------------------------------------------------------------
# In Python, users can define custom exceptions by creating a new class. 

# This exception class has to be derived, either directly or indirectly, 
# from the built-in Exception class. 

# Most of the built-in exceptions are also derived from this class.

#---------------------------------------------------------------------------------------
# define Python user-defined exceptions
class CustomError(Exception):
  pass

#---------------------------------------------------------------------------------------

# we have created a user-defined exception called CustomError which inherits from 
# the Exception class. This new exception, like other exceptions, can be raised 
# using the raise statement with an optional error message.


try:
  num = int(input("Enter a number :  "))
  if num < 10:
    raise CustomError('The value is too small')
except CustomError as e:
  print(f"Error : {e}")
else:
  print(f"The {num} is greater than 10")