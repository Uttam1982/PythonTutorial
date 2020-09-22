# dir() function
# Now that you have the class declared, you can use the dir() function to list its members:

class Animal:
  pass

a = Animal()
print(dir(a))

print()

o = object() 
print(dir(o))

#-------------------------------------------------------------------------------
class Dog:
  name ='snoowy'

  def __init__(self,age):
    self.age = age
  
  def bark(self):
    pass


print()
d = Dog(12)
print(dir(d))
