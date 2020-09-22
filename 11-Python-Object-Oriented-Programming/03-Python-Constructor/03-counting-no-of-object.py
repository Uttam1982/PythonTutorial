# Counting the number of objects of a class
# The constructor is called automatically when we create the object of the class.


class Employee:
  """This is an Employee Class"""
  
  #class attribute
  count = 0

  #Parameterized constructor have two attributes id and name
  def __init__(self, id, name):
    self.id = id
    self.name = name
    Employee.count += 1

  def display(self):
    print(f"#Id: {self.id}, Name: {self.name}")


emp1 = Employee("Sam", 23)
emp2 = Employee("Ben", 21)
emp3 = Employee("Joe", 22)

print(f"The number of employees: {Employee.count}")

