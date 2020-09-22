#--------------------------------------------------------------------------------------------
# 7. Consider Comprehensions As Alternatives
#--------------------------------------------------------------------------------------------

# If the purpose of the iteration is to create a new list, dictionary, or set object 
# from the iterable, we should consider the comprehension technique, which is more 
# performant and more concise.

#--------------------------------------------------------------------------------------------
# LIST
# iterable
numbers = [1,2,3,4,5]

# initialize an empty list
square_list = list()

# typical for loop
print("\n# typical for loop")
for i in numbers:
  square_list.append(i * i)
print(square_list)

#using list comprehension
print("#using list comprehension")
square_list = [ x * x  for x in numbers]
print(square_list)
print("\n--------------------------------")

#--------------------------------------------------------------------------------------------
# SET
#initialize an empty set
square_set = set()

# typical for loop
print("\n# typical for loop")
for i in numbers:
  square_set.add(i*i)
print(square_set)

#using list comprehension
print("#using set comprehension")
square_set = { x * x for x in numbers }
print(square_set)
print("\n--------------------------------")

#--------------------------------------------------------------------------------------------
# DICTIONARY 

# initialize a dictionary
square_dict = dict()

# typical for loop
print("\n# typical for loop")
for i in range(1, len(numbers)+1):
  square_dict[i] = i * i
print(square_dict)


# using dictionary comprehension
print("#using set comprehension")
square_dict = {x : x*x for x in numbers}
print(square_dict)

#--------------------------------------------------------------------------------------------

# The list comprehension has the following format: 
#     [expr for item in iterable]
# which is the preferred way to create a list object compared to the for loop.


# The set comprehension has the following format: 
#     {expr for item in iterable}
# which is the preferred way to create a set object from an iterable compared to the for loop.


# The dictionary comprehension has the following format: 
#     {key_expr: value_expr for item in iterable}. 
# Similarly, it’s the preferred way to create a dict object from an iterable.

#--------------------------------------------------------------------------------------------

