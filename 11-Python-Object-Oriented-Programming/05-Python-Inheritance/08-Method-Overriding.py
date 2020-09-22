#---------------------------------------------------------------------------------------
# Method Overriding
#---------------------------------------------------------------------------------------
# 1. We can provide some specific implementation of the parent class method in our 
#    child class. 

# 2. When the parent class method is defined in the child class with some specific 
#    implementation, then the concept is called method overriding. 

# 3. We may need to perform method overriding in the scenario where the different 
# definition of a parent class method is needed in the child class.

#----------------------------------------------------------------------------------------

class Animal:
  def eat(self):
    print("Animal eats both grass and meat")

class Tiger(Animal):
  def eat(self):
    print("Tiger eats only meat")

tiger = Tiger()
tiger.eat()

#----------------------------------------------------------------------------------------
# Real Life Example of method overriding

class Bank:
  def getroi(self):
    return 10

class SBI(Bank):
  def getroi(self):
    return 8

class HDFC(Bank):
  def getroi(self):
    return 7

b1 = Bank()
print("Bank Rate of interest : ",b1.getroi())

b2 = SBI()
print("SBI Rate of interest : ",b2.getroi())

b3 = HDFC()
print("HDFC Rate of interest : ",b3.getroi())

#----------------------------------------------------------------------------------------

