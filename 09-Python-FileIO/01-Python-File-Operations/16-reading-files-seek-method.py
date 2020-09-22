#**************************************************************************************
# Modifying file pointer position
#**************************************************************************************

#<file-ptr>.seek(offset[, from) 
# Python provides us the seek() method which enables us to modify the file pointer 
# position externally.

# The seek() method accepts two parameters:

# offset: It refers to the new position of the file pointer within the file.
# from: It indicates the reference position from where the bytes are to be moved. 

# If it is set to 0, the beginning of the file is used as the reference position. 
# If it is set to 1, the current position of the file pointer is used as the reference position. 
# If it is set to 2, the end of the file pointer is used as the reference position.



#**************************************************************************************
try:
  f = open('file1.txt','r',encoding='utf-8')
  print('file opened successfully!')
  
  #initially the filepointer is at 0   
  print("The filepointer is at byte :",f.tell())

  #changing the file pointer location to 23.  
  f.seek(23)

  #current position (in number of bytes).
  print("The filepointer is at byte :",f.tell())

  print(f.read())
  

finally:
  print('file closed successfully...')
  f.close()

