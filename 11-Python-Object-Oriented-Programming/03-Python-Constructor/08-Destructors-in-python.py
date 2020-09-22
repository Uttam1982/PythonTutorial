#Destructors in Python
# 1. Destructors are called when an object gets destroyed. 

# 2. In Python, destructors are not needed as much needed in C++ 
#    because Python has a garbage collector that handles memory 
#    management automatically.

# 3. The __del__() method is a known as a destructor method in Python. 
# It is called when all references to the object have been deleted 
# i.e when an object is garbage collected.

#-----------------------------------------------------------------------------------------

class Employee:

  # initializing
  def __init__(self):
    print("Employee Created")

  # Deleting (calling constructor)
  def __del__(self):
    print('Destructor called , Employee deleted')


obj = Employee()

del obj

#-----------------------------------------------------------------------------------------


