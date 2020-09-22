# Polymorphism

# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). 
# However we could use the same method to color any shape. This concept is called Polymorphism.

class Parrot:
  def fly(self):
    print('Parrort cannot fly')
  
  def swim(self):
    print("Parrot can't swim")

class Penguin:
  def fly(self):
    print("Pengiun can't fly")

  def swim(self):
    print("Pengiun can swim")  

#interface
def fly_test(bird):
  bird.fly()
  bird.swim()

parrot = Parrot()
penguin = Penguin()

fly_test(parrot)
fly_test(penguin)

# interface class

class Flying_Test:
  def fly_test(self,bird):
    bird.fly()
    bird.swim()

print("\nusing class as an interface")
parrot = Parrot()
penguin = Penguin()

test = Flying_Test()
test.fly_test(parrot)
test.fly_test(penguin)