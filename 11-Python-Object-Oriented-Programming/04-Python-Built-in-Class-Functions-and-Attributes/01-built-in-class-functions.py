# Python built-in class functions
#---------------------------------------------------------------------------------------------

# 1. getattr(obj,name,default):	It is used to access the attribute of the object.

# 2. setattr(obj,name,value): 	It is used to set a particular value to the specific attribute 
#                               of an object.

# 3. delattr(obj, name):       	It is used to delete a specific attribute.

# 4. hasattr(obj, name):       	It returns true if the object contains some specific attribute.

#---------------------------------------------------------------------------------------------

class Student:
  def __init__(self, id, name,age):
    self.id = id
    self.name = name
    self.age = age

  def display(self):
    print(f"#Id: {self.id}, Name: {self.name}, Age: {self.age}")


s1 = Student(10,'Alex',23)
s1.display()

# Access the attributes
print("Id: ",getattr(s1,'id'))
print("Name: ",getattr(s1,'name'))
print("Age: ",getattr(s1,'age'))

# set the attribute values
setattr(s1,'name','Alex-new')
setattr(s1,'age',24)

s1.display()
print("Name: ",getattr(s1,'name'))
print("Age: ",getattr(s1,'age'))

# prints true if the student contains the attribute with name id  
print('Student has id attribute: ',hasattr(s1,'id'))
print('Student has name attribute: ',hasattr(s1,'name'))
print('Student has age attribute: ',hasattr(s1,'age'))

delattr(s1,'id')

print('Student has id attribute: ',hasattr(s1,'id')) #False
# AttributeError: 'Student' object has no attribute 'id'
print(getattr(s1,'id'))





