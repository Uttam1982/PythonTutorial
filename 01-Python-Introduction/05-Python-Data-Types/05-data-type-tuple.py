# Python Tuple
# - Tuple is an ordered sequence of items same as a list.
# - The only difference is that tuples are immutable. 
# - Tuples once created cannot be modified.

# - Tuples are used to write-protect data 
# - faster than lists as they cannot change dynamically.

# - It is defined within parentheses () where items are separated by commas.

t = (5,'program', 1+3j)
print('t = ',t)

# We can use the slicing operator [] to extract items but we cannot change its value.
# t[1]=  'program'
print('t[1]= ',t[1])

# t[0:3] =  (5, 'program', (1+3j))
print('t[0:3] = ',t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10