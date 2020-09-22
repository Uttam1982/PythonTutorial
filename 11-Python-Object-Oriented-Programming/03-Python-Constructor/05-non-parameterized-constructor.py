# Python Non-Parameterized Constructor
#------------------------------------------------------------------------------------

# The non-parameterized constructor uses when we do not want 
# to manipulate the value or the constructor that has only self as an argument.

#------------------------------------------------------------------------------------

class Employee:

  # Non-Parameterized constructor
  def __init__(self):
    print("Employee non-parameterized constructor")
  
  def display(self,name):
    print(f"Hi, {name} !")

# Employee class is instantiated
emp1 = Employee()
emp2 = Employee()


emp1.display('Sam')
emp2.display('Sara')