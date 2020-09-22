#**************************************************************************************
# Writing to Files in Python
#**************************************************************************************

# In order to write into a file in Python, we need to open it different mode
# 1. in write: w, 
# 2. append: a 
# 3. exclusive creation: x 


# We need to be careful with the w mode, as it will overwrite 
# into the file if it already exists. Due to this, all the 
# previous data are erased.

# Writing a string or sequence of bytes (for binary files) is done using the write() method. 
# This method returns the number of characters written to the file.

#**************************************************************************************

try:

  # open the file1.txt in append mode. 
  f = open('file1.txt','a',encoding='utf-8')
  print('file opened successfully in append mode')

  # appending the content to the file  
  f.write("This is the fourth line\n")
  
finally:
  print('file closed successfully!')
  f.close()
