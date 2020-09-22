# class method:
# The class method is different from the static method. 
# Here, the class method can access or modify class state.
# We pass cls as an argument that points to the class 
# and not the object instance — when the method is called.

class Pizza:
  # class variabe
  info = "This is a class variable"

  # defining slots
  __slots__ = ['type','size','shape']

  # instance attribute
  def __init__(self,type,size,shape='round'):
    self.type = type
    self.size = size
    self.shape = shape

  #instance method
  def display(self):
    print(f"{obj.type} pizza ordered of {obj.size} and {obj.shape}")

  # static method
  @staticmethod
  def get_veg_ingredients():
    list_ingredients = ['onion','mushroom','jalapeneos','peper','olives']
    return list_ingredients
  
  # class method
  @classmethod
  def determine_size(cls, type, size, shape):
    if size <= 14:
      return cls(type,'medium',shape)
    else:
      return cls(type,'large',shape)


# instantiate the class
obj = Pizza.determine_size(type='veggie',size = 12, shape='square')
obj.display()

# We generally use class method to create factory methods. 
# Factory methods return class object ( similar to a constructor ) 
# for different use cases.


# As we see above, one can use the method separately, but it needs all 
# the arguments that the class to which it belongs expects. The size was 
# determined as “medium” based on the entered number. We define them 
# using @classmethod.



