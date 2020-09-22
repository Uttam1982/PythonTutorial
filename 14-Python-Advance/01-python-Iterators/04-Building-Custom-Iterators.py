#--------------------------------------------------------------------------------------
# Building Custom Iterators
#--------------------------------------------------------------------------------------
# Building an iterator from scratch is easy in Python. 
# We just have to implement the __iter__() and the __next__() methods.

# The __iter__() method returns the iterator object itself. 
# If required, some initialization can be performed.

# The __next__() method must return the next item in the sequence. 
# On reaching the end, and in subsequent calls, it must raise StopIteration.

#--------------------------------------------------------------------------------------

class PowTwo:

  """Class to implement an iterator
  of power of two """

  # instance attribute
  def __init__(self,max = 0):
    self.max = max

  # implement iter method
  def __iter__(self):
    self.n = 0
    return self
  
  # implement next method
  def __next__(self):
    if self.n <= self.max:
      result = 2 ** self.n
      self.n += 1
      return result
    else:
      raise StopIteration


# Instantaite a PowTwo class
powTwo = PowTwo(3)

# get an iterator using iter
iter_obj = iter(powTwo)

# iterate through using next
try:
  print(next(iter_obj))
  print(next(iter_obj))
  print(next(iter_obj))
  print(next(iter_obj))
  print(next(iter_obj))
except StopIteration as e:
  print(f"Error : {e}")





