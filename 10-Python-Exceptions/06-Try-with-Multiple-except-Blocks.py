#--------------------------------------------------------------------------------
# Try with multiple except blocks
#--------------------------------------------------------------------------------

# If multiple errors may arise after the execution of one try block, 
# we may use multiple except blocks to handle them.

# Since every exception in Python inherits from the base Exception class, 

#--------------------------------------------------------------------------------
try:
  print(age)
except NameError as error:
  print(f"Error: {error}")
except:
  print("Seeems like something else went wrong")


# Since every exception in Python inherits from the base Exception class, 
# we can also perform the above task in the following way:

try:
  print(age)
except NameError as error:
  print(f"Error: {error}")
except Exception as e:
  print(f"Seeems like something else went wrong {e}")


#--------------------------------------------------------------------------------
import sys

def linux_interaction():
  assert('linux' in sys.platform),"Function can run only in linux system"
  print("Inside the method")


try:
  linux_interaction()
except AssertionError as error:
  print(f"Error : {error}")
except:
  print("Seeems like something else went wrong")

#--------------------------------------------------------------------------------

# Since every exception in Python inherits from the base Exception class, 
# we can also perform the above task in the following way:

try:
  linux_interaction()
except AssertionError as error:
  print(f"Error : {error}")
except Exception as e:
  print(f"Seeems like something else went wrong {e}")