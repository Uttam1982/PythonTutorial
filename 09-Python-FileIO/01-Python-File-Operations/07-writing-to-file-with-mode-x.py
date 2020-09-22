#**************************************************************************************
# Writing to Files in Python
#**************************************************************************************

# In order to write into a file in Python, we use one of the following access modes 
# with the function open().


# 1. x: it creates a new file with the specified name. 
#       It causes an error a file exists with the same name. 

# 2. a: It creates a new file with the specified name if no such file exists. 
#       It appends the content to the file if the file already exists with the specified name.

# 3. w: It creates a new file with the specified name if no such file exists. 
#       It overwrites the existing file. 


# We need to be careful with the w mode, as it will overwrite 
# into the file if it already exists. Due to this, all the 
# previous data are erased.

# Writing a string or sequence of bytes (for binary files) is done using the write() method. 
# This method returns the number of characters written to the file.

#**************************************************************************************

try:

  # Create a new file if no such file exists. Will give error if file exists 
  
  f = open('file1.txt','x',encoding='utf-8')
  # f = open('file2.txt','x',encoding='utf-8')
  if f:  
    print('file opened successfully in xclusive creation mode')
  
  
  f.write("File is opened in xclusive mode \n")
  

finally:
  print('file closed successfully!')
  f.close()
