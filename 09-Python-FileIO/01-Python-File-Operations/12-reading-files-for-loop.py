#**************************************************************************************
# Reading Files in Python
#**************************************************************************************

# To read a file in Python, we must open the file in reading r mode.

# We can read the file using for loop. 

#**************************************************************************************
try:
  #open the file.txt in read mode. causes error if no such file exists.  
  f = open('file1.txt','r',encoding='utf-8')
  print('file opened successfully!\n')

  for l in f:   
    print(l) ## l contains each line of the file    

finally:
  print('file closed successfully...')
  f.close()

