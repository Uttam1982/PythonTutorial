# In Python, a class can be created by using the keyword class, 
# followed by the class name

class Employee:
  """This is an Employee class"""

  # contains two fields as Employee id, and name.
  id = 10
  name = "Sam"

  #display the information of the Employee.
  def display(self):
    print(f"Id = {self.id}, Name = {self.name}")

  #display the information of the Employee.
  def show(self):
    print("This is show method")
    self.display()
    


print(f"#Id: {Employee.id}")
print(f"Name: {Employee.name}")

print(f"display Method: {Employee.display}")

#gives us the docstring of that class.
print(f"Docs string: {Employee.__doc__}")


#------------------------------------------------------------------------------
# 1. Here, the self is used as a reference variable, 
# 2. which refers to the current class object. 
# 3. It is always the first argument in the function definition. 
# 4. However, using self is optional in the function call.