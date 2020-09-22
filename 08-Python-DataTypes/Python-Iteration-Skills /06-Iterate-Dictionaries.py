#------------------------------------------------------------------------------------------------
# 6. Iterate Dictionaries
#------------------------------------------------------------------------------------------------

# Dictionaries are a very common data type that stores data in the form of key-value pairs. 
# Because of the implementation using hashes, it’s very fast to look up and retrieve items 
# from dictionaries, and thus they’re the favorite data structure for many developers. 
# The storage of key-value pairs gives us different options to iterate dictionaries.

#------------------------------------------------------------------------------------------------

numbers = {1:"one",2:"two",3:"three",4:"four"}

print("Print all the keys")
for key in numbers.keys():
  print(key)

print("Print all the values")
for val in numbers.values():
  print(val)

print("Print all the keys and values")
for key, val in numbers.items():
  print(key, val)


# To iterate the keys, we’ll just use the keys() method on the dictionary object. 
# Alternatively, we can just use the dictionary object itself as the iterable, 
# which is just a syntactical sugar for the view object created by the keys() method.

# To iterate the values, we’ll just use the values() method.
# To iterate the items in the form of key-value pairs, we’ll use the items() method.




