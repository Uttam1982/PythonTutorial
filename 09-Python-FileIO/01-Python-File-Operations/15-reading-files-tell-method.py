#**************************************************************************************
# File Pointer positions
#**************************************************************************************

# tell() method

# Python provides the tell() method which is used to print the byte number at which 
# the file pointer currently exists

#**************************************************************************************
try:
  f = open('file1.txt','r',encoding='utf-8')
  if f:  
    print('file opened successfully')
  
  #initially the filepointer is at 0   
  print("The filepointer is at byte :",f.tell())

  print(f.read(5))
  print(f.read(5))

  #current position (in number of bytes).
  print("The filepointer is at byte :",f.tell())

  print(f.read())
  print("After reading, the filepointer is at:",f.tell())    

finally:
  print('file closed successfully...')
  f.close()

