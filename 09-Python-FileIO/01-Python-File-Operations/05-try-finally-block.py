#**************************************************************************************
# Closing Files in Python
#**************************************************************************************

# If an exception occurs when we are performing some operation with the file, 
# the code exits without closing the file.

# A safer way is to use a try...finally block.

#**************************************************************************************

# opens the file file.txt in read mode 
try:
   f = open('file1.txt','r',encoding='utf-8')
   # perform file operations
   if f:
      print('File Opened successfully!')

  
finally:
   #closes the opened file
   print("Closing the file")
   f.close()


# This way, we are guaranteeing that the file is properly closed 
# even if an exception is raised that causes program flow to stop.

# The best way to close a file is by using the with statement