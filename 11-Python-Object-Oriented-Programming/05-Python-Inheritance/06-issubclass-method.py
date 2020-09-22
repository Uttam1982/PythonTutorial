class Animal:
  def eat(self):
    print("eating....")

class Dog(Animal):
  def bark(self):
    print("barking....")

class Cat(Animal):
  def meow(self):
    print("meowing....")

cat = Cat()
cat.meow()
cat.eat()

#AttributeError: 'Cat' object has no attribute 'bark'
# cat.bark()

#--------------------------------------------------------------------------------------
# The issubclass(sub,sup) method
#--------------------------------------------------------------------------------------

# The issubclass(sub, sup) method is used to check the relationships 
# between the specified classes. It returns true if the first class 
# is the subclass of the second class, and false otherwise.

#--------------------------------------------------------------------------------------

print("Dog is sub class of Animal: ",issubclass(Dog,Animal))
print("Cat is sub class of Animal: ",issubclass(Cat,Animal))
print("Animal is sub class of Cat: ",issubclass(Animal,Cat))


