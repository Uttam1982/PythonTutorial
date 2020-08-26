# Python bytearray()
# The bytearray() method returns a bytearray object which is an array of the given bytes

# The syntax of bytearray() method is:
# bytearray([source[, encoding[, errors]]])

# The bytearray() method returns a bytearray object which is mutable
# sequence of integers in the range 0 <= x < 256

# If you want immutable version use bytes() method
#******************************************************************************************

#bytearray() Parameters
# bytearray() takes three optional parameters:

# 1. source (Optional) - source to initialize the array of bytes.
# 2. encoding (Optional) - if the source is a string, the encoding of the string.
# 3. errors (Optional) - if the source is a string, the action to take when the 
# encoding conversion fails (Read more: String encoding)


#The source parameter can be used to initialize the byte array in the following ways:

#String:	  Converts the string to bytes using str.encode() 
#           Must also provide encoding and optionally errors

#Integer	  Creates an array of provided size, all initialized to null
#Object	    A read-only buffer of the object will be used to initialize the byte array
#Iterable	  Creates an array of size equal to the iterable count and initialized to the 
#           iterable elements Must be iterable of integers between 0 <= x < 256

# No source (arguments): 	Creates an array of size 0.
#******************************************************************************************

#Return value from bytearray()
#bytearray() method returns an array of bytes of the given size and initialization values.

#******************************************************************************************

#Example 1: Array of bytes from a string

string ='Python is interesting'

arr = bytearray(string,'utf-8')
print(arr)


# Example 2: Array of bytes of given integer size

size = 5
arr = bytearray(size)
print(arr)

# Example 3: Array of bytes from an iterable list
list = [1,2,3,4,5]
arr = bytearray(list)
print(arr)