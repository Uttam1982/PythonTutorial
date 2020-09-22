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
  """Base class for other exceptions"""
  pass

class ValueTooSmallError(CustomError):
  """Raised when the input value is too small"""
  pass

class ValueTooLarge(CustomError):
  """Raised when the input value is too large"""
  pass


# you need to guess this number
number = 10

# # user guesses a number until he/she gets it right
while True:
  try:
    num = int(input("Enter a number :  "))
    if num < 10:
      raise ValueTooSmallError
    elif num > 10:
      raise ValueTooLarge
    else:
      break
  except ValueTooSmallError:
    print("This value is too small, Try again!\n")
  except ValueTooLarge:
    print("This value is too large , Try again!\n")
  
print("Congratulation !, you have guess it correctly.")



