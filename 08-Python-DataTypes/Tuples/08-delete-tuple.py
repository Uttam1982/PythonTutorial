# Deleting a Tuple
# As discussed above, we cannot change the elements in a tuple. 
# It means that we cannot delete or remove items from a tuple.

# Deleting a tuple entirely, however, is possible using the keyword del.

my_tuple = (12,23,34,45,56,67,78,89,90)

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
#del my_tuple[3]

# Can delete an entire tuple
del my_tuple

#NameError: name 'my_tuple' is not defined
print(my_tuple)

