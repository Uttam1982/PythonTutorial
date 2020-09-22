# Parameterized Constructor

class Employee:
  """This is an Employee Class"""
  
  #Parameterized constructor have two attributes id and name
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def display(self):
    print(f"#Id: {self.id}, Name: {self.name}")


emp1 = Employee("Sam", 23)
emp2 = Employee("Ben", 21)

emp1.display()
emp2.display()




