#------------------------------------------------------------------------------
# Python Default Constructor
#------------------------------------------------------------------------------

# When we do not include the constructor in the class or forget to declare it, 
# then that becomes the default constructor. It does not perform any task but 
# initializes the objects.

#------------------------------------------------------------------------------

class Employee:
  id = 10
  name = 'Alex'

  def display(self):
    print(f"#Id: {self.id}, Name: {self.name}")


emp = Employee()
emp.display()