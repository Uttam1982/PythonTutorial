# ------------------------------------------------------------------------------------
# Iterating Through an Iterator
# ------------------------------------------------------------------------------------
# We use the next() function to manually iterate through all the items of an iterator. 

# When we reach the end and there is no more data to be returned, 

# it will raise the StopIteration
# ------------------------------------------------------------------------------------

#define a list
numbers = ["one","two","three"]

# get an iterator using iter()
my_iter = iter(numbers)

#iterate through it using next()

# output : one
print(next(my_iter))

# output : two
print(next(my_iter))

# output : three
print(next(my_iter))

# output : This will raise an error StopIteration
print(next(my_iter))