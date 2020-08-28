# Removing elements from Dictionary
#********************************************************************************************
# There are multiple ways you can remove items in a dictionary
# 1. pop() method : This method removes an item with the provided key and returns the value.

# 2. The popitem() method: can be used to remove and return an arbitrary (key, value) 
#    item pair from the dictionary.

# 3. clear() method : All the items can be removed at once

# 4. del keyword: to remove individual items or the entire dictionary itself.
#********************************************************************************************

my_dict = {1:'Sam',2:'Ben',3:'Joe',4:'Sara',5:'Alice'}

#using pop() method
print("original my_dict= ",my_dict)
# removes an item with the provided key
print("my_dict.pop(2)= ",my_dict.pop(2))
print("updated my_dict= ",my_dict)

# using pop() method
# TypeError: pop expected at least 1 arguments, got 0

# print("my_dict.pop()= ",my_dict.pop())    # key value **required
# print("updated my_dict= ",my_dict)

#********************************************************************************************

#using popitem() method
# remove an arbitrary item, return (key,value)
print("my_dict.popitem()= ",my_dict.popitem())
print("updated my_dict= ",my_dict)

#********************************************************************************************

# del keyword: to remove individual items
del my_dict[4]
print("updated my_dict= ",my_dict)

#********************************************************************************************
# remove all items
my_dict.clear()
print("updated my_dict= ",my_dict)

#********************************************************************************************

#using popitem() method
# Raises KeyError if the dictionary is empty.

# print("my_dict.popitem()= ",my_dict.popitem())
# print("updated my_dict= ",my_dict)

#********************************************************************************************

# delete the dictionary itself
del my_dict

# NameError: name 'my_dict' is not defined
print("updated my_dict= ",my_dict)

#********************************************************************************************