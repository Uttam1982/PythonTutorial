#**************************************************************************************
# Reading Files in Python
#**************************************************************************************

# To read a file in Python, we must open the file in reading r mode.

# There are various methods available for this purpose. 

# fileobj.read(<size>)    
# We can use the read(size) method to reads the number of bytes to be read from 
# the file starting from the beginning of the file. 

# If the size parameter is not specified, it reads and returns up to the end of the file.

#**************************************************************************************
try:
  #open the file.txt in read mode. causes error if no such file exists.  
  f = open('file1.txt','r',encoding='utf-8')
  
  if f:
    print('file opened successfully!')

  # #stores all the data of the file into the variable content 
  content = f.read(5)

  # prints the type of the data stored in the file   
  print(type(content))

  #prints the content of the file    
  print(content)

  print(f.read(5))


finally:
  print('file closed successfully...')
  f.close()

