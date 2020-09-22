#------------------------------------------------------------------------------------
# Methods
#------------------------------------------------------------------------------------

# Methods are functions defined inside the body of a class. 
# They are used to define the behaviors of an object.

#------------------------------------------------------------------------------------
# Example  : Creating Methods in Python

class Student:

  #instance attribute
  def __init__(self, name, age):
    self.name = name
    self.age = age

  #instance method
  def sing(self, song):
    print(f"{self.name} sings {song}")

  def dance(self):
    print(f"{self.name} is dancing")

# instantiate a student object
sara = Student('Sara', 23)

# access the methods
sara.sing('Jack and Jill went up the hill')
sara.dance()



