#count() method
# The count() method returns the number of times the specified element appears in the list.

# Example 1: Use of count()

# output : 3
my_list = [10,20,30,40,20,50,20]
print(my_list.count(20))


# Example 2: Count Tuple and List Elements Inside List
my_list = [1,(2,3),(2,3),[4,5]]

# Count Tuple : 2
print(my_list.count((2,3)))

# Count list : 1 
print(my_list.count([4,5]))