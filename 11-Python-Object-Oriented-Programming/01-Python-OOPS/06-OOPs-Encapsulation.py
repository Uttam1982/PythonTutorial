#------------------------------------------------------------------------------------
# Encapsulation
#------------------------------------------------------------------------------------
# Using OOP in Python, we can restrict access to methods and variables. 
# This prevents data from direct modification which is called encapsulation. 
# In Python, we denote private attributes using underscore as the prefix i.e 
# single _ or double __.

#------------------------------------------------------------------------------------
# Example : Data Encapsulation in Python

class Computer:
  def __init__(self):
    self.__maxprice = 900
  
  def sell(self):
    print(f"Selling price : {self.__maxprice}")

  def setMaxPrice(self, price):
    self.__maxprice = price
  

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter method
c.setMaxPrice(1000)
c.sell()

#------------------------------------------------------------------------------------
#  We tried to modify the price. However, we can't change it because 
# Python treats the __maxprice as private attributes.

# As shown, to change the value, we have to use a setter function 
# i.e setMaxPrice() which takes price as a parameter.

#------------------------------------------------------------------------------------
