#------------------------------------------------------------------------------------------
# Catching Specific Exceptions in Python
#------------------------------------------------------------------------------------------
# A try clause can have any number of except clauses to handle different exceptions, 
# however, only one will be executed in case an exception occurs.

# We can use a tuple of values to specify multiple exceptions in an except clause. 
# Here is an example pseudo code.

#------------------------------------------------------------------------------------------

try:
  # do something
  pass
except ValueError as ve:
  # handle ValueError exception
  pass
except(TypeError, ZeroDivisionError):
  #handle multiple exception
  # Typeerror and ZeroDivisionError
  pass
except:
  # handle all exceptions
  pass