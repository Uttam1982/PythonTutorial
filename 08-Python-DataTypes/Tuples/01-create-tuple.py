# Python Tuple
# 1. A tuple in Python is similar to a list. 
# 2. The difference between the two is that we cannot change the elements of a tuple 
#    once it is assigned whereas we can change the elements of a list.

# Creating a Tuple
# 1. A tuple is created by placing all the items (elements) inside parentheses (), 
#    separated by commas. 
# 2. The parentheses are optional, however, it is a good practice to use them.
# 3. A tuple can have any number of items and they may be of different types 
#    (integer, float, list, string, etc.).

#***************************************************************************************

# Empty tuple
my_tuple = ()
print("empty tuple: ",my_tuple)

# Tuple having integers
my_tuple = (1,2,3,4)
print("tuple having integers: ",my_tuple)

# tuple with mixed datatypes
my_tuple = ('Sara',21,34.5)
print("tuple with mixed datatypes: ",my_tuple)

# nested tuple
my_tuple = ('Sara',[1,2,3],(4,5,6))
print("nested tuple: ",my_tuple)

#***************************************************************************************
#A tuple can also be created without using parentheses. 
# This is known as tuple packing.

my_tuple = 1,'sara', 34.5
print('tuple created without using parentheses: ',my_tuple)

# unpacking tuple
id,name,bmi = my_tuple
print("id:",id," name:",name," bmi:",bmi)




