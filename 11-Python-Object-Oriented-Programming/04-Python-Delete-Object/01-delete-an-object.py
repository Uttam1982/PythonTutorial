# Delete the Object
# We can delete the properties of the object or object itself by using the del keyword.
# Any attribute of an object can be deleted anytime, using the del statement. 

class Employee:
  # class variables
  id = 10
  name = 'Alex'

  def display(self):
    print(f"#Id{self.id} - Name: {self.name}")


# creating the instance of Employee class
emp = Employee()

# deleting the property of the object
print("deleting the id property")


del Employee.id
# #output: AttributeError: 'Employee' object has no attribute 'id'
emp.display()


del Employee.display
# #output AttributeError: 'Employee' object has no attribute 'display'
emp.display()

# deleting the object itelf
print('deleting the object itelf')
del emp

#output : NameError: name 'emp' is not defined
emp.display()

#---------------------------------------------------------------------