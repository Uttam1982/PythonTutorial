#The copy() method returns a shallow copy of the list.

# A list can be copied using the = operator.
my_list = [1,2,3,4]
c_list = my_list
print('my_list: ',my_list)
print('copy_list: ',c_list)

# The problem with copying lists in this way is that if you modify c_list, 
# my_list is also modified.

c_list.append(5)
print('modified my_list: ',my_list)
print('modified copy_list: ',c_list)

# However, if you need the original list unchanged when the new list is modified, 
# you can use the copy() method.
#*************************************************************************************************
## shallow copy using the copy method

my_list = [1,2,3,4]

#The copy() method returns a new list. It doesn't modify the original list.
c_list = my_list.copy()
c_list.append(5)
print('modified my_list: ',my_list)
print('modified copy_list: ',c_list)

#*************************************************************************************************

#Example : Copy List Using Slicing Syntax

my_list = [1,2,3,4]

# shallow copy using the slicing syntax
c_list = my_list[:]

c_list.append(5)
print('modified my_list: ',my_list)
print('modified copy_list: ',c_list)

#*************************************************************************************************

