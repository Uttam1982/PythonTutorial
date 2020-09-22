#**************************************************************************************
# Reading Files in Python
#**************************************************************************************

# To read a file in Python, we must open the file in reading r mode.

# readlines() function
# Python provides also the readlines() method which is used for the reading lines. 
# It returns the list of the lines till the end of file(EOF) is reached.

#**************************************************************************************
try:
  # open the file.txt in read mode. causes error if no such file exists.  
  f = open('file1.txt','r',encoding='utf-8')
  print('file opened successfully!\n')

  # returns the list of the lines till the end of file(EOF) is reached into the variable content
  content = f.readlines()
  
  # prints the content of the file in    
  print(content)

  # prints the content of the file using for loop
  for line in content:
    print(line)

finally:
  print('file closed successfully...')
  #closes the opened file   
  f.close()

