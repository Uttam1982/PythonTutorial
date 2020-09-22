#----------------------------------------------------------------------------------
# Python Inheritance
#----------------------------------------------------------------------------------

# Inheritance is an important aspect of the object-oriented paradigm. Inheritance 
# provides code reusability to the program because we can use an existing class to 
# create a new class instead of creating it from scratch.

# In inheritance, the child class acquires the properties and can access all the 
# data members and functions defined in the parent class. A child class can also 
# provide its specific implementation to the functions of the parent class.

#----------------------------------------------------------------------------------

class Animal:
  def eat(self):
    print("eating....")

class Dog(Animal):
  def bark(self):
    print('barking....')

dog = Dog()
dog.eat()
dog.bark()
  