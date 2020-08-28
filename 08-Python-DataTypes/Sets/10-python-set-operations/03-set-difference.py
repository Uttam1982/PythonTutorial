# Set Difference

# 1. Difference of the set B from set A(A - B) is a set of elements 
#    that are only in A but not in B. 
# 2. Similarly, B - A is a set of elements in B but not in A.

# 3. Difference is performed using - operator. 
# 4. Same can be accomplished using the difference() method.

#------------------------------------------------------------------------------------------------

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator
print("A - B: ",A-B)
print("B - A: ",B-A)

# use of difference function
print("A - B: ",A.difference(B))
print("B - A: ",B.difference(A))