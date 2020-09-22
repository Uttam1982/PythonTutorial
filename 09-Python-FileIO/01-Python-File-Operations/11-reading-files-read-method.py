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
  print('file opened successfully!\n')

  #prints the content of the file    
  print(f.read())

finally:
  print('file closed successfully...')
  f.close()

