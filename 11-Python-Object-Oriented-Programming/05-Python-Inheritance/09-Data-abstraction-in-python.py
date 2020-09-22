# Data abstraction in python

# Abstraction is an important aspect of object-oriented programming. 
# In python, we can also perform data hiding by adding the double underscore (___) 
# as a prefix to the attribute which is to be hidden. 

# After this, the attribute will not be visible outside of the class through the object.

class Employee:
  # private class attribute
  __count = 0
  def __init__(self):
    Employee.__count += 1
    # private instance variable
    self.__num = 10
  
  def get__Count(self):
    print(f"class variable: {self.__count} ")
    

  def get__num(self):
    print(f"instance variable: {self.__num}")

e1 = Employee()

try:
  print(e1.__count)
except AttributeError as e:
  print(e)
finally:
  e1.get__Count()


try:
  print(e1.__num)
except AttributeError as e:
  print(e)
finally:
  e1.get__num()




