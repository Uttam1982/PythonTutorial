# How to change or add elements to a list?

# 1. Lists are mutable, meaning their elements can be changed unlike string or tuple.
# 2. We can use the assignment operator (=) to change an item or a range of items.

#***************************************************************************************
# Correcting mistake values in a list
my_list = [3,5,7,9]

#change the 1st element
my_list[0] = 1
print(my_list)

# change 2nd to 4th items
my_list[1:4] = [4,6,8]
print(my_list)



