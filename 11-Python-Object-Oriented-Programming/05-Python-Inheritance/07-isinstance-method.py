class Animal:
  def eat(self):
    print("eating....")

class Dog(Animal):
  def bark(self):
    print("barking....")

class Cat(Animal):
  def meow(self):
    print("meowing....")

cat_obj = Cat()
cat_obj.meow()
cat_obj.eat()

#AttributeError: 'Cat' object has no attribute 'bark'
# cat.bark()

#--------------------------------------------------------------------------------------
# The isinstance (obj, class) method
#--------------------------------------------------------------------------------------
# The isinstance() method is used to check the relationship between the objects and classes. 
# It returns true if the first parameter, i.e., obj is the instance of the second parameter, 
# i.e., class.

#--------------------------------------------------------------------------------------

print("'cat_obj' is instance Cat class: ",isinstance(cat_obj,Cat))
print("'cat_obj' is instance Dog class: ",isinstance(cat_obj,Dog))

