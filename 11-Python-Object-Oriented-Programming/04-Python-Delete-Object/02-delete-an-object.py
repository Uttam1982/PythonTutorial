#-----------------------------------------------------------------------
# using del keyword and delattr in-built class functions
#-----------------------------------------------------------------------

class Student:
  def __init__(self, id, name,age):
    self.id = id
    self.name = name
    self.age = age
  
  def display(self):
    print(f"Id: {self.id}, Name: {self.name}, Age: {self.age}")

#-----------------------------------------------------------------------

# create an instance object of Student class
s1 = Student(10,'Bob',23)
s1.display()

#-----------------------------------------------------------------------
# deleting the attribute id
del s1.id

# AttributeError: 'Student' object has no attribute 'id'
# print(getattr(s1,'id'))

# AttributeError: 'Student' object has no attribute 'id'
# s1.display()
#-----------------------------------------------------------------------

delattr(s1,'name')

# AttributeError: 'Student' object has no attribute 'name'
# print(getattr(s1,'name'))

#-----------------------------------------------------------------------
del s1.display

# AttributeError: display
# s1.display()

#----------------------------------------------------------------------- 
# deleteing the complete object
del s1

#NameError: name 's1' is not defined
s1.display()

#-----------------------------------------------------------------------


