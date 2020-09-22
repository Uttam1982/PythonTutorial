#---------------------------------------------------------------------------------------
# Creating an instance of the class
#---------------------------------------------------------------------------------------
# A class needs to be instantiated if we want to use the class attributes 
# in another class or method. 
# A class can be instantiated by calling the class using the class name.

# The syntax to create the instance of the class is given below.

      # <object-name> = <class-name>(<arguments>) 

class Employee:
  """This is an Employee class"""

  # contains two fields as Employee id, and name.
  id = 10
  name = "Sam"

  #display the information of the Employee.
  def display(self):
    print(f"Id = {self.id}, Name = {self.name}")

  

# creating the instance of Employee class
emp = Employee()

# calling the instance method
emp.display()

#output: <function Employee.display>
print(Employee.display)

#output: <bound method Employee.display of <__main__.Employee object>
print(emp.display)

#----------------------------------------------------------------------------------------
# Attributes may be data or method. 
# Methods of an object are corresponding functions of that class.

# This means to say, since Employee.display is a function object (attribute of class), 
# emp.display will be a method object.

