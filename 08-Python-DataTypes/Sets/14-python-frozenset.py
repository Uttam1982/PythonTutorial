# Python Frozenset

# Frozenset is a new class that has the characteristics of a set,
# its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.

# Sets being mutable are unhashable, so they can't be used as dictionary keys
# frozensets are hashable and can be used as keys to a dictionary.

# Frozensets can be created using the frozenset() function.

# This data type supports methods like copy(), difference(), intersection(), 
# isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). 

# Being immutable, it does not have methods that add or remove elements.

# Create frozensets
A = frozenset([1,2,3,4])
B = frozenset([3,4,5,6])

print(A.isdisjoint(B)) # False
print(A.difference(B)) # frozenset({1, 2})

#frozensets are immutable sets

#attributeError: 'frozenset' object has no attribute 'add'
#A.add(5)



