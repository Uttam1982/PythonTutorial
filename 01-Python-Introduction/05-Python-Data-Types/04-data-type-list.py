# Python List
# - List is an ordered sequence of items.
# - It is very flexible. 
# - Lists are mutable, meaning, the value of elements of a list can be altered.
# - All the items in a list do not need to be of the same type.

# Declaring a list
# Items separated by commas are enclosed within brackets [ ].

alist = [1,2.2,'python']
print(alist)

# Use the slicing operator [ ] to extract an item or a range of items from a list. 
# The index starts from 0 in Python.

a = [10,20,30,40,50,60,70,80,90]

#Extract the 3rd element in the list
print("a[2] = ",a[2])

#Extract the first three element
print("a[0:3] = ",a[0:3] )
print("a[:3] = ",a[:3] )

#Extract the last element
print("a[8] = ",a[8])
print("a[-1] = ",a[-1])

#Extract the last three elements
print("a[6:10] = ",a[6:10] )
print("a[6:] = ",a[6:] )
print("a[-3:] = ",a[-3:] )

# Lists are mutable
a[2]= 31
print(a)