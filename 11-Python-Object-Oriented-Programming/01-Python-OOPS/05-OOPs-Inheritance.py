# Inheritance
# Inheritance is a way of creating a new class for using details of an existing 
# class without modifying it. The newly formed class is a derived class (or child class). 
# Similarly, the existing class is a base class (or parent class).

#-------------------------------------------------------------------------------------------

# Parent class
class Bird:
  def __init__(self):
    print("Bird is ready")

  def whoisthis(self):
    print("Bird")

  def swim(self):
    print("Swim faster")

class Penguin(Bird):
  def __init__(self):
    # call super() function
    super().__init__()
    print("Penguin is ready")

  def whoisthis(self):
    print("Penguin")

  def run(self):
    print("Run faster")


penguin = Penguin()
penguin.whoisthis()
penguin.swim()
penguin.run()

