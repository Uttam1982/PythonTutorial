# append() method
# The append() method adds an item to the end of the list.
# We can add one item to a list using the append() method

# Appending and Extending lists in Python

# Example 1: Add one element on the list
my_list = [2,4,6,8]
my_list.append(1)
print(my_list)                        # [2, 4, 6, 8, 1]


# Example 2: Adding List to a List
my_list.append([1,3,5,7])
print(my_list)                        # [2, 4, 6, 8, 1, [1, 3, 5, 7]]


# If you need to add items of a list to another list 
# (rather than the list itself), use the extend() method.

