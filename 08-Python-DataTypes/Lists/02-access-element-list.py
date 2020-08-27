# How to access elements from a list?

# 1. We can use the index operator [] to access an item in a list. 
# 2. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.
# 3. Trying to access indexes other than these will raise an IndexError. 
# 4. The index must be an integer. 
# 5. We can't use float or other types, this will result in TypeError.


# List indexing

my_list = [23,45,67,89,99]

print(my_list[0])

print(my_list[2])

print(my_list[4])

# print(my_list[4.0]) # Error! Only integer can be used for indexing

print(my_list[5]) #IndexError: list index out of range

# Nested List
n_list = ["Sara",23,[90,98,87,79]]

# Nested indexing
print(n_list[2])

print(n_list[2][1])


print(n_list[2][3])

print(n_list[2][4]) #IndexError: list index out of range






