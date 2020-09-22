# Python Special Functions

# Class functions that begin with double underscore __ are called special functions in Python.

# These functions are not the typical functions that we define for a class. The __init__() function we defined above is one of them. It gets called every time we create a new object of that class.

# There are numerous other special functions in Python. Visit Python Special Functions to learn more about them.

#https://docs.python.org/3/reference/datamodel.html#special-method-names

# Using special functions, we can make our class compatible with built-in functions.

#----------------------------------------------------------------------------------------

class Point:
  def __init__(self,x = 0,y = 0):
    self.x = x
    self.y = y
  
p1 = Point(3,4)

# Output : <__main__.Point object at 0x7ff1e6436350>
print(p1)

# Output : <__main__.Point object at 0x7ff1e6436350>
print(str(p1))

# Output : <__main__.Point object at 0x7ff1e6436350>
print(format(p1))

#----------------------------------------------------------------------------------------
# Suppose we want the print() function to print the coordinates of the Point object 
# instead of what we got. We can define a __str__() method in our class that controls 
# how the object gets printed.


class Point1:
  def __init__(self,x = 0,y = 0):
    self.x = x
    self.y = y

  def __str__(self):
    return "{0},{1}".format(self.x, self.y)
  
p1 = Point1(3,4)

# Output : 3,4
print(p1)

# Output : 3,4
print(str(p1))

# Output : 3,4
print(format(p1))


#----------------------------------------------------------------------------------------