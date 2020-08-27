# We can use + operator to combine two tuples. This is called concatenation.
# We can also repeat the elements in a tuple for a given number of times using the * operator.

# Both + and * operations result in a new tuple.

my_tuple = (1,2,3)
print(my_tuple)

#create a new tuple
print(my_tuple + (4,5,6))

#original tuple dosen't change
print(my_tuple)

# Repeat
print(('python',)* 3)


