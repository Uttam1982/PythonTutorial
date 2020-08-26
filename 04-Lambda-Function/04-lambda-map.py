# map() function

# 1. The map() function in Python takes in a function and a list.

# 2. The function is called with all the items in the list and a new list 
#    is returned which contains items returned by that function for each item.
#*******************************************************************************************

# Program to double each item in a list using map()
my_list = [1,6,9,2,5,3,4]
new_list = list(map(lambda x: x * 2,my_list))
print(new_list)


# Program to square each item in a list using map()
my_list = [1,6,9,2,5,3,4]
new_list = list(map(lambda x: x ** 2,my_list))
print(new_list)