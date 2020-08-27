# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on.

my_tuple = ('p','y','t','h','o','n')

print("my_tuple: ",my_tuple)
print("my_tuple type: ",type(my_tuple))

# output n
print(my_tuple[-1])

# output p
print(my_tuple[-6])

# output IndexError: list index out of range
#print(my_tuple[-7])
