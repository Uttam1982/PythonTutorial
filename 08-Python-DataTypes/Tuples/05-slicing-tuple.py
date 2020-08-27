# # Accessing tuple elements using slicing
# We can access a range of items in a tuple by using the slicing operator colon :.

my_tuple = (12,23,34,45,56,67,78,89,90)

#element 2nd to 4th
print('element 2nd to 4th: ',my_tuple[2:5])

#elements beginning to 2nd
print('elements beginning to 2nd: ',my_tuple[:2])
print('elements beginning to 2nd: ',my_tuple[:-7])

# elements 8th to end
print('elements 8th to end: ',my_tuple[7:])
print('elements 8th to end: ',my_tuple[-2:])

#elements beginning to end
print('elements beginning to end: ',my_tuple[:])

