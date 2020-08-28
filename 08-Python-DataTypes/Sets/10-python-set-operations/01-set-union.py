# Python Set Operations

# Sets can be used to carry out mathematical set operations like 
# 1. union, 
# 2. intersection, 
# 3. difference and 
# 4. symmetric difference. 
# We can do this with operators or methods.

#Set Union
# 1. Union of A and B is a set of all elements from both sets.
# 2. Union is performed using | operator. 
# 3. Same can be accomplished using the union() method.

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print(A|B)

#use union function
print(A.union(B))

#use union function
print(B.union(A))

