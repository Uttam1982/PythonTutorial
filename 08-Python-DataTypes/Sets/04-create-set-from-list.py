# we can make set from a list

my_set = set([1,2,3,4,3,2])
print("set from a list: ",my_set)


# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error

# my_set = set([1,2,3,4,[3,4]])
# print("set from a list: ",my_set)

# my_set = {1,2,3,4,[3,4]}
# print("set cannot have mutable items: ",my_set)
