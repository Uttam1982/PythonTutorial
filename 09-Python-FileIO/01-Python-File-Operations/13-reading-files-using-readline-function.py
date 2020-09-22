#********************************************************************************************
# Reading Files in Python
#********************************************************************************************

# To read a file in Python, we must open the file in reading r mode.

#-------------------------------------------------------------------------------------------
# readline() function
#-------------------------------------------------------------------------------------------
# Python facilitates to read the file line by line by using a function readline() method. 
# The readline() method reads the lines of the file from the beginning, i.e., if we 
# use the readline() method two times, then we can get the first two lines of the file.

#********************************************************************************************
try:
  #open the file.txt in read mode. causes error if no such file exists.  
  f = open('file1.txt','r',encoding='utf-8')
  print('file opened successfully!\n')

  #stores all the data of the file into the variable content1
  content1 = f.readline()
  content2 = f.readline()
  
  #prints the content of the file    
  print(content1)
  print(content2)

finally:
  print('file closed successfully...')
  #closes the opened file   
  f.close()

