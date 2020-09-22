# __str__
# __str__ is quite similar to __repr__ above. __str__ can be overridden 
# and allows more customization unless like repr which cannot be.

class Pizza:
  #class variable
  info = 'This is a Pizza class'

  #instance attribute:
  def __init__(self,type_):
    self.type_ = type_
    # instance variables inside methods  
    self.shape = 'round'

  # instance method:
  def __str__(self):
    return f"Type: {self.type_} , Shape : {self.shape}"

# instantiate the class
obj = Pizza('Veggie')
print(obj)

# As seen above, unless like __repr__, the object needs to be 
# passed to the print function to display the variables. 
# __str__ is the opposite of __repr__and is considered as 
# an “informal” string representation of an object. It is 
# used mainly for creating output for regular users.