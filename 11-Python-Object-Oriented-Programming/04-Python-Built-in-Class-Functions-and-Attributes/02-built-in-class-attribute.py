#-------------------------------------------------------------------------------------------------
# Built-in class attributes
#-------------------------------------------------------------------------------------------------
# 1. __dict__	: It provides the dictionary containing the information about the class namespace.

# 2. __doc__ :	It contains a string which has the class documentation 

# 3. __name__ :	It is used to access the class name.

# 4. __module__ :	It is used to access the module in which, this class is defined.

# 5. __bases__ :	It contains a tuple including all base classes.

#-------------------------------------------------------------------------------------------------

class Student:
  """This is a Student class"""

  def __init__(self,id,name,age):
    self.id = id
    self.name = name
    self.age = age

  def display(self):
    print(f"{self.id} -- {self.name} -- {self.age}")


s1 = Student(10,'Alex',21)

print(s1.__doc__)
print(s1.__dict__)
print(s1.__module__)
