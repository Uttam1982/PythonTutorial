# The try and except Block: Handling Exceptions

# The try and except block in Python is used to catch and handle exceptions. 
# Python executes code following the try statement as a “normal” part of the program. 

# The code that follows the except statement is the program’s response to any 
# exceptions in the preceding try clause.

#--------------------------------------------------------------------------------
try:
  print(age)
except:
  print("The variable is not defined")

#--------------------------------------------------------------------------------
import sys

def linux_interaction():
  assert('linux' in sys.platform),"Function can run only in linux system"
  print("Inside the method")


try:
  linux_interaction()
except:
  print('The linux_interaction() function was not executed\n')

#--------------------------------------------------------------------------------

import sys

randomlist = ['a',0,2]

for val in randomlist:
  try:
    print(f"The value is: {val}")
    r = 1/int(val)
    break
  except:
    print(f"Opps!, {sys.exc_info()[0]}, has occured")
    print('Next entry')
    print()
    
print(f"The reciprocal of {val} is {r}")
  