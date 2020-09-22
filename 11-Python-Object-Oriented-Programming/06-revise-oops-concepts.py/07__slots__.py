# __slots__
# __slots__ is quite similar to __dict__. 
# This is one of the best features, often unused by the Python community. 
# If the data is passed to __init__ and used mainly for storing data,
#  __slots__ can help to optimize the performance of the class.

class Pizza:
  #class variable 
  info = 'This is a Pizza class'

  #Defining slots
  __slots__ = ['type','size','shape']

  # instance attribute
  def __init__(self,type,size):
    self.type = type
    self.size = size
    # instance variables inside methods  
    self.shape = 'round'

#instantiate the class
obj = Pizza(type='veggie',size='large')
print(obj.__slots__)

# To dive a bit deep in detail, __dict__ wastes a lot of RAM. 
# This is a great way to tell Python not to use __dict__ and 
# only use a fixed set of attributes. For heavy RAM work, 
# some people have seen a reduction of 40–50% in RAM usage[2] 
# by using __slots__.



