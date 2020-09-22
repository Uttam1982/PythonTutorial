#--------------------------------------------------------------------------------
# The AssertionError Exception
#--------------------------------------------------------------------------------
# We assert that a certain condition is met. 

# If this condition turns out to be True, then that is excellent! 
# The program can continue. 

# If the condition turns out to be False, you can have the program 
# throw an AssertionError exception.

#--------------------------------------------------------------------------------

import sys

print("system platform: ",sys.platform)
assert('linux' in sys.platform),"This code runs in linux only"


# If you run this code on a Linux machine, the assertion passes. 
# If you were to run this code on any other  Windows or Mac machine, 
# the outcome of the assertion would be False


# In this example, throwing an AssertionError exception is the last thing 
# that the program will do. 
# The program will come to halt and will not continue. 

#--------------------------------------------------------------------------------
# What if that is not what you want?