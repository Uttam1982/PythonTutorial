# __call__
# __call__ is run as soon as a method is called. 
# It basically takes action once the object is initiated. 
# __call__ is useful when an instance needs to often change state.

class Pizza:
  #class attribute
  info= "This is a Pizza Class"

  #instance attribute:
  def __init__(self, type_):
    self.type_ = type_
    # instance variables inside methods  
    self.shape ='round'

  #instance method
  def __call__(self,shape = None):
    if shape:
      self.shape = shape
      return print(f'submitting a {self.type_} pizza order with change shape ----{self.shape}')
    else:
      print(f'submitting a {self.type_} pizza order with default shape ----{self.shape}')


#instantiate a class
obj = Pizza(type_ = 'veggie')

# #calling the class 
obj()
obj('square')


# We can see that the default value of shape is ‘round’. However, 
# I was able to change the shape by passing a value to the object 
# after initiating it. Try passing empty brackets and check the output!