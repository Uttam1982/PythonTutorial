# pop() method
# ----------------------------------------------------------------------------------
# pop() method to remove an item at the given index.
# returns the removed item.

# The pop() method removes and returns the last item if the index is not provided.
# The argument passed to the method is optional. If not passed, the default index -1 
# is passed as an argument (index of the last item). 
# This helps us implement lists as stacks (first in, last out data structure).

#*************************************************************************************
my_list = [12,23,34,45,56,67,78,89,90]
print("list: ", my_list)

# remove an item at the given index.

# output 23
print('Return value: ',my_list.pop(1))
print('Updated list: ',my_list)

# output 90
print('Return value: ',my_list.pop())
print('Updated list: ',my_list)

# output 90
print('Return value: ',my_list.pop(-1))
print('Updated list: ',my_list)


# output IndexError: pop index out of range
print('Return value: ',my_list.pop(10))
print('Updated list: ',my_list)

