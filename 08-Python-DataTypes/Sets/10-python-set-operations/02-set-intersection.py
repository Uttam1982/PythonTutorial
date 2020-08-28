# Set Intersection

# 1. Intersection of A and B is a set of elements that are common in both the sets.
# 2. Intersection is performed using & operator. 
# 3. Same can be accomplished using the intersection() method.

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use of & operator
print(A&B)

# use of intersection function on A
print(A.intersection(B))

# use of intersection function on B
print(B.intersection(A))

