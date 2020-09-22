# __dict__
# Python has an internal dictionary called __dict__ that holds all 
# the internal variables. It is a simple way to inspect the internal 
# details of the variables.

class Pizza:
  #class variable
  info = "This is a pizza class"

  #instance attribute:
  def __init__(self, type, size):
    self.type = type
    self.size = size
    # instance variables inside methods  
    self.shape = 'round'
  
#instantaite the  class
obj = Pizza('veggie', 'large')
print(obj.__dict__)

# One can also change the variables directly by using __dict__ attribute
obj.__dict__['size'] = 'medium'
print(obj.__dict__)


