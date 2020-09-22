# Create a new attribute

# attributes of an object can be created on the fly. 


class Employee:
  """This is an Employee Class"""
  
  #Parameterized constructor have two attributes id and name
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def display(self):
    print(f"#Id: {self.id}, Name: {self.name}")

# Create a new Employee object
emp1 = Employee("Sam", 23)

# Call display() method
# Output: #Id: Sam, Name: 23
emp1.display()

# Create another Employee object
# and create a new attribute 'attr'
emp2 = Employee("Ben", 21)
emp2.attr = 10

# Output : #Id: Ben, Name: 21, Attr: 10
print(f"#Id: {emp2.id}, Name: {emp2.name}, Attr: {emp2.attr}")

# but emp1 object doesn't have attribute 'attr'
# AttributeError: 'Employee' object has no attribute 'attr'
print(f"#Id: {emp1.id}, Name: {emp1.name}, Attr: {emp1.attr}")

# An interesting thing to note in the above step is that attributes of an object 
# can be created on the fly. 

# We created a new attribute attr for object emp2 and read it as well. 
# But this does not create that attribute for object emp1.




