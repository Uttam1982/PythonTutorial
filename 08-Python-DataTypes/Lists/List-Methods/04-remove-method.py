# Python List remove()
#**************************************************************************************************
# 1. The remove() method removes the first matching element (which is passed as an argument) 
# from the list.
# 2. list.remove(element)
# 3. If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
# 4. The remove() doesn't return any value (returns None).

#**************************************************************************************************

# Example : Remove element from the list
my_list = [10,20,30,40,20,30]
print(my_list)

# remove the element 10
my_list.remove(10)
# output [20, 30, 40, 20, 30]
print(my_list)

#**************************************************************************************************
# Example : remove on list having duplicate elements
# remove the element 10
my_list.remove(20)
# output [30, 40, 20, 30]
print(my_list)

#**************************************************************************************************
#Example: Deleting element that doesn't exist

my_list = [10,20,30,40,20,30]

#output ValueError: list.remove(x): x not in list
my_list.remove(50)

#**************************************************************************************************
# 1. If you need to delete elements based on the index (like the fourth element), 
# you can use the pop() method.

# 2. Also, you can use the Python del statement to remove items from the list.




