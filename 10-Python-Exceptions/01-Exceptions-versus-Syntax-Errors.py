#--------------------------------------------------------------------------------
# Exceptions versus Syntax Errors
#--------------------------------------------------------------------------------

# Syntax errors occur when the parser detects an incorrect statement. 
# Observe the following example:

# SyntaxError: invalid syntax

# print(0/0))


# The arrow indicates where the parser ran into the syntax error. 
# In this example, there was one bracket too many. 
#--------------------------------------------------------------------------------

# Remove it and run your code again:

print(0/0)   # ZeroDivisionError: division by zero


# This time, you ran into an exception error. 

# This type of error occurs whenever syntactically correct Python code 
# results in an error. 

# The last line of the message indicated what type of exception error you ran into.

#--------------------------------------------------------------------------------