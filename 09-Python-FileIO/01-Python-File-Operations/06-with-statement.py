#**************************************************************************************
# Closing Files in Python
#**************************************************************************************

# The best way to close a file is by using the with statement. 

# This ensures that the file is closed when the block inside the with statement is exited.

# We don't need to explicitly call the close() method. It is done internally.

#**************************************************************************************

with open('file1.txt','r', encoding='utf-8') as f:
  # perform file operations
  pass

