#**************************************************************************************
# Get Current Directory
#**************************************************************************************

# We can get the present working directory using the getcwd() method of the os module.
# This method returns the current working directory in the form of a string. 
# We can also use the getcwdb() method to get it as bytes object.

#**************************************************************************************

import os

print("Get Current Working Directory: ",os.getcwd())

print("Get Current Working Directory in bytes: ",os.getcwdb())

