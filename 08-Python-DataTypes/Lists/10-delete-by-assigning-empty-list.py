# we can also delete items in a list by assigning an empty list to a slice of elements.

my_list = [12,23,34,45,56,67,78,89,90]
print(my_list)

my_list[2:4] =[]
# output [12, 23, 56, 67, 78, 89, 90]
print(my_list)

my_list[2:5] =[]
# output [12, 23, 89, 90]
print(my_list)

