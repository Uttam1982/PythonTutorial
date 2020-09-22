# static method

# Some methods, do not need to be modified or pass any class argument necessarily, 
# to be used. It makes sense for them to be part of the class but not the object 
# of the class. In other words, they know nothing about the class state. Such methods 
# are known as static method

class Pizza:
  #class variable 
  info ="This is a pizza class"

  #Defining slots 
  __slots__ = ['type','size','shape']

  # instance attribute

  def __init__(self, type, size):
    self.type = type
    self.size = size
    # instance variables inside methods  
    self.shape = 'round'

  # static method
  @staticmethod
  def get_veg_ingredients():
    list_ingredients = ['onions','peper','olives','jalapeneos','mushroom']
    return list_ingredients

# Get the static method without instantiaating the class

print(Pizza.get_veg_ingredients())


# As we see above, we can directly use static method without even initiating the class. 
# We define such methods using @staticmethod. We mainly use to create utility functions.

