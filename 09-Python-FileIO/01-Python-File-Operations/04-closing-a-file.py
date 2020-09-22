#**************************************************************************************
# Closing Files in Python
#**************************************************************************************
# 1. When we are done with performing operations on the file, 
#    we need to properly close the file.

# 2. Closing a file will free up the resources that were tied with the file. 

# 3. It is done using the close() method available in Python.

# 4. Python has a garbage collector to clean up unreferenced objects 
#    but we must not rely on it to close the file.

#**************************************************************************************

# opens the file file.txt in read mode   
f = open('file1.txt','r',encoding='utf-8')

if f:
   print('File Opened successfully!')

#closes the opened file
print("Closing the file")
f.close()

#**************************************************************************************

# This method is not entirely safe. 

# If an exception occurs when we are performing some operation with the file, 
# the code exits without closing the file.

# A safer way is to use a try...finally block.
