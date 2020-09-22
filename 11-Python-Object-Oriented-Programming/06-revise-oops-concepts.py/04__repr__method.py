# __repr__
# __repr__ is mainly used to see the values assigned to our variables. 
# It can be defined as below:

class Pizza:

  #class variable
  info = "This is a class variable"

  #instance attribute
  def __init__(self, type_):
    self.type_ = type_ 
    # instance variables inside methods  
    self.shape = 'round'

  # instance method

  def __repr__(self):
    return f"Type: {self.type_}, Shape:  {self.shape}"

# Instantiate the class
obj = Pizza(type_ = 'veggie')

#obj
print(obj)

# Even though __repr__ is considered as “official” string representation 
# of an object this is mainly used for debugging, mainly used by developers.


