# How to slice lists in Python?
# We can access a range of items in a list 
# by using the slicing operator :(colon).

# List slicing in Python
my_list = [12,23,34,45,56,67,78,89,90]

# elements 3rd to 5th
print('elements 3rd to 5th: ',my_list[2:5])

# elements beginning to 4th
print('elements beginning to 4th: ',my_list[:4])
print('elements beginning to 4th: ',my_list[:-5])


# elements 6th to end
print('elements 6th to end: ',my_list[5:])
print('elements 6th to end: ',my_list[-4:])

#elements beginning to end
print('elements beginning to end: ',my_list[:])

