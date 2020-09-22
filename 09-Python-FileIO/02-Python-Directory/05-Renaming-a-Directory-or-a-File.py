#-----------------------------------------------------------------------------------------
# Renaming a Directory or a File
#-----------------------------------------------------------------------------------------
# The rename() method can rename a directory or a file.

# For renaming any directory or file, the rename() method takes in two basic arguments: 
# the old name as the first argument and the new name as the second argument.


#    rename(current-name, new-name)  

#-----------------------------------------------------------------------------------------
import os

# Renaming a Directory
os.rename('test','new-test')


# Renaming the file
# os.rename('file1.txt','new-file1.txt')