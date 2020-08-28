# Modifying a set in Python

# 1. Sets are mutable. 
# 2. However, since they are unordered, indexing has no meaning.
# 3. We cannot access or change an element of a set using indexing or slicing. 
#    Set data type does not support it.
# 4. We can add a single element using the add() method, 
# 5. Add multiple elements using the update() method. 
# 6. The update() method can take tuples, lists, strings or other sets as its argument. 
# 7. In all cases, duplicates are avoided.

#********************************************************************************************
my_set = {1,2,3,4}
print("original set: ",my_set)

# 1. You will get an error
# TypeError: 'set' object is not subscriptable
#print(my_set[0])

# 2. Add a single element using the add() method
my_set.add(5)
print("modified set using add(): ",my_set)

# 3. Add multiple elements using the update() method. 
my_set.update([4,5,6,7])
print("modified set using update(): ",my_set)

# 4. Add list and set
my_set.update([4,5,6,7],{6,7,8,9})
print("modified set using update(): ",my_set)

# 5. Add list,tuple and set
my_set.update([4,5,6,7],(2,3,10),{6,7,8,9})
print("modified set using update(): ",my_set)