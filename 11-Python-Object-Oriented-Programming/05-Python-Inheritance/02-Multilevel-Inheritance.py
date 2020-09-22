class Animal:
  def eat(self):
    print("eating....")

class Dog(Animal):
  def bark(self):
    print('barking....')

class Puppy(Dog):
  def weep(self):
    print("weeping....")

puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.weep()

print()

dog = Dog()
dog.eat()
dog.bark()