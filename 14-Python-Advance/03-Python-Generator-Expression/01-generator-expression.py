#--------------------------------------------------------------------------------------------
# Python Generator Expression
#--------------------------------------------------------------------------------------------

# Similar to the lambda functions which create anonymous functions, 
# generator expressions create anonymous generator functions.

# The syntax for generator expression is similar to that of a list comprehension in Python. 
# But the square brackets are replaced with round parentheses.

# The major difference between a list comprehension and a generator expression is that 
# a list comprehension produces the entire list while 
# the generator expression produces one item at a time.

# They have lazy execution ( producing items only when asked for ). 
# For this reason, a generator expression is much more memory efficient 
# than an equivalent list comprehension.

#--------------------------------------------------------------------------------------------

# initialize a list
lst = [2,3,4,5]
# square each item using list comprehension
squares = [x * x for x in lst ]

# Output : [4, 9, 16, 25]
print(squares)


# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
squares_gen = (x * x for x in lst)

# Output: <generator object <genexpr> at 0x7ff747c485d0>
print(squares_gen)

# We can see above that the generator expression did not produce the required result immediately. 
# Instead, it returned a generator object, which produces items only on demand.

# Output: 4
print(next(squares_gen))
# Output: 9
print(next(squares_gen))
# Output: 16
print(next(squares_gen))
# Output: 25
print(next(squares_gen))
# output : StopIteration
print(next(squares_gen))
