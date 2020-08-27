# How to delete or remove elements from a list?
# We can delete one or more items from a list using the keyword del. 
# It can even delete the list entirely.

my_list = [12,23,34,45,56,67,78,89,90]
print(my_list)

#delete 2nd element 
del my_list[1]
print(my_list)

# delete multiple items
del my_list[1 : 5]
print(my_list)

#index out of range 
# del my_list[10]
# print(my_list)


# Example 2: Emptying the List Using del
del my_list[:]
print(my_list)


# delete entire list
del my_list
print(my_list)



