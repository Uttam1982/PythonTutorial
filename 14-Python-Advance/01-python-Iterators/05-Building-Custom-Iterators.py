class yrange:
  """class to implement an iterator
  to find range of a given number
  """

  # instance attribute
  def __init__(self,n):
    self.n = n
    self.i = 0

  # implement the iter menthod
  def __iter__(self):
    return self

  # implement the next method
  def __next__(self):
    if self.i < self.n:
      i = self.i
      self.i += 1
      return i
    else:
      raise StopIteration


# instantiate a yrange
y = yrange(3)

# get the iter object
iter_obj = iter(y)

# display the next elemnt using next

# Output : 0
print(next(iter_obj))

# Output : 1
print(next(iter_obj))

# Output : 2
print(next(iter_obj))

# Output : Error StopIteration
# print(next(iter_obj))

print(list(yrange(5)))

#----------------------------------------------------------------------

class zrange:
  """class to implement iterator
  to find in range starting at 10
  """
  
  def __init__(self,n):
    self.n = n
  
  
  def __iter__(self):
    self.start = 10
    return self


  def __next__(self):
    start = self.start
    
    if start > self.n:
      raise StopIteration
    else:
      self.start = start + 1
      return start



# Value of zrange should be greater than 10
for i in zrange(15):
  print(i, end=" ")

print()

print(list(zrange(14)))

#----------------------------------------------------------------------

      
