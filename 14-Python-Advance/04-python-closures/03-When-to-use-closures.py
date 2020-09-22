#---------------------------------------------------------------------------------------
# When to use closures?
#---------------------------------------------------------------------------------------
# Closures can avoid the use of global values and provides some form of data hiding. 
# It can also provide an object oriented solution to the problem.

# When there are few methods (one method in most cases) to be implemented in a class, 
# closures can provide an alternate and more elegant solution.

# But when the number of attributes and methods get larger, it's better to implement a class.

#---------------------------------------------------------------------------------------

def make_square_of(n):
  def square():
    return n ** 2
  
  return square

square_5 = make_square_of(5)
print(square_5())

#---------------------------------------------------------------------------------------

def make_multiple_of(n):
  def multiplier(x):
    return  n * x
  
  return multiplier

times_3 = make_multiple_of(9)
print(times_3(3))  # 3 * 9 = 27

times_5 = make_multiple_of(9)
print(times_5(5))  # 5 * 9 = 45

# pipeleine
print(times_5(times_3(3))) # (9 * (3 * 9))

#---------------------------------------------------------------------------------------

# All function objects have a __closure__ attribute that returns 
# a tuple of cell objects if it is a closure function. 
# Referring to the example above, we know times3 and times5 are closure functions.

print(make_multiple_of.__closure__)
print(times_3.__closure__)

#---------------------------------------------------------------------------------------

# The cell object has the attribute cell_contents which stores the closed value.
print(times_3.__closure__[0].cell_contents)
print(times_5.__closure__[0].cell_contents)

#---------------------------------------------------------------------------------------

