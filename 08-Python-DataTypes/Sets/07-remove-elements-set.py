# Removing elements from a set

# 1. A particular item can be removed from a set using the methods discard() and remove().

# 2. discard() function: leaves a set unchanged if the element is not present in the set.

# 3. remove() function: will raise an error in such a condition 
#    (if element is not present in the set).

# initialize my set 
my_set = {12,23,34,45,56,67}
print(my_set)

# discard element 23
my_set.discard(23)
print(my_set)

# not present in my_set
# discard element 65
my_set.discard(65)
print(my_set)

# remove element 56
my_set.remove(56)
print(my_set)

# not present in my_set
# remove element 50
# output : KeyError: 50
my_set.remove(50)
print(my_set)