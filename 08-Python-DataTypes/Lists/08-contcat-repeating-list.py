# Other Ways to Extend a List
# 1. the + operator

# We can also use + operator to combine two lists. This is also called concatenation.
# The * operator repeats a list for the given number of times.

# Concatenating two list
my_list = [1,2,3,4]
new_list = my_list + [5,6,7,8]

# output : [1, 2, 3, 4, 5, 6, 7, 8]
print(new_list)

# output : [1, 2, 3, 4]
print(my_list)


#2. the list slicing syntax
x = [10, 20]
y = [30, 40]

x[len(x):] = y

# Output: [10, 20, 30, 40]
print('x =', x)


# repeating lists
#--------------------------------------------
# output : [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(my_list * 3) 