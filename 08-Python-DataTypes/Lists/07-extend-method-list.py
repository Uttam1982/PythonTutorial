# extend() method
# The extend() method adds all the elements of an iterable (list, tuple, string etc.) 
# to the end of the list.

# add several items using extend() method.

# Appending and Extending lists in Python

# Example 1: adding multiple elements
my_list = [2,4,6,8]
my_list.extend([10,12])
print(my_list)


# Example 2: Add Elements of Tuple and Set to List
my_tuple = (14,16)
my_list.extend(my_tuple)
print(my_list)          #[2, 4, 6, 8, 10, 12, 14, 16]


my_set = {18,20}
my_list.extend(my_set)  
print(my_list)          #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]







