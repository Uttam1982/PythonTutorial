# Set Symmetric Difference

# 1. Symmetric Difference of A and B is a set of elements in A and B but not in both 
#    (excluding the intersection).
# 2. Symmetric difference is performed using ^ operator. 
# 3. Same can be accomplished using the method symmetric_difference().

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use of ^ operator
print("A^B: ",A^B)
print("B^A: ",B^A)

# use of symmetric_difference() function
print("A^B: ",A.symmetric_difference(B))
print("B^A: ",B.symmetric_difference(A))

