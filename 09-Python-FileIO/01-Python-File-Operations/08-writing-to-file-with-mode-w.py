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

  # open the file1.txt in write mode. Create a new file if no such file exists.
  # overwriting the content of the file if file exist 

  f = open('file1.txt','w',encoding='utf-8')
  if f:  
    print('file opened successfully in write mode')


  f.write("This is the first line\n")
  f.write("This is the second line\n")
  f.write("This is the third line\n")

finally:
  print('file closed successfully!')
  f.close()
