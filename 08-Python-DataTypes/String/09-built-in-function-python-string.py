# Built-in functions to Work with Python
# Various built-in functions that work with sequence work with strings as well.

# Some of the commonly used ones are enumerate() and len(). 

# The enumerate() function returns an enumerate object. 
# It contains the index and value of all the items in the string as pairs. 

# Similarly, len() returns the length (number of characters) of the string.

str1 = 'python'

#enumerate
list_enumerate = list(enumerate(str1))
print('list(enumerate(str1)= ',list_enumerate)

#Find the length of string
print("len(str1)= ",len(str1))