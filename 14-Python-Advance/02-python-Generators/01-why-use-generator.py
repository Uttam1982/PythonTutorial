#----------------------------------------------------------------------------------------------
# Generators in Python
#----------------------------------------------------------------------------------------------
# There is a lot of work in building an iterator in Python. 
# We have to implement a class with __iter__() and __next__() method, 
# keep track of internal states, and raise StopIteration when there 
# are no values to be returned.

# This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

# Python generators are a simple way of creating iterators. 
# All the work we mentioned above are automatically handled by generators in Python.

# A generator is a function that returns an object (iterator) 
# which we can iterate over (one value at a time).

#----------------------------------------------------------------------------------------------
# Create Generators in Python
#----------------------------------------------------------------------------------------------

# It is fairly simple to create a generator in Python. 
# It is as easy as defining a normal function, but with a yield statement 
# instead of a return statement.

# If a function contains at least one yield statement 
# (it may contain other yield or return statements), it becomes a generator function.


# The difference is that while a return statement terminates a function entirely, 

# ** yield statement pauses the function saving all its states and later continues 
# from there on successive calls.

#----------------------------------------------------------------------------------------------
# Differences between Generator function and Normal function
#----------------------------------------------------------------------------------------------

# 1. Generator function contains one or more yield statements.

# 2. When called, it returns an object (iterator) but does not start execution immediately.

# 3. Methods like __iter__() and __next__() are implemented automatically. 
#    So we can iterate through the items using next().

# 4. Once the function yields, the function is paused and the control is transferred 
#    to the caller.

# 5. Local variables and their states are remembered between successive calls.

# 6. Finally, when the function terminates, StopIteration is raised automatically on 
#    further calls.

#----------------------------------------------------------------------------------------------

# https://anandology.com/python-practice-book/iterators.html
