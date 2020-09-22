# python program to demonstrate
# use of class method and static method
from datetime import date

class Person:
  #instance attribute
  def __init__(self, name,age):
    self.name = name
    self.age = age
  
  # A class method to create Person object by birth year
  @classmethod
  def fromBithYear(cls,name, year):
    return cls(name, date.today().year - year)

  # static method to check the person is adult or not
  @staticmethod
  def isAdult(age):
    if age > 18:
      print("You are adult")
    else:
      print("You are not adult")

  #instance method
  def display_age(self):
    print(f"{self.name} your age is: {self.age}")

#instantiating a class 
person1 = Person('Sam',16)

#calling class method to create object
person2 = Person.fromBithYear('Ben',1990)

person1.display_age()
person2.display_age()

# calling static method
Person.isAdult(person1.age)
Person.isAdult(person2.age)
