# Python bin()

# The bin() method converts and returns binary equivalent strings of a given integer.
# bin() method takes a single parameter, 
# num - an integer number whose binary eqivalent is to be calculated 
# if the parameter isn't an integrer, it has to implement __index__() method to return an integer

# ************************************************************************************************

num = 5
print('The binary equivalent string of ',num,' is: ',bin(num))

# num = '1'
# print('The binary equivalent string of ',num,' is: ',bin(num))

#If not specified an integer, it raises a TypeError exception 
# highlighting the type cannot be interpreted as an integer.

# ************************************************************************************************

# Example 2: Convert an object to binary implementing __index__() method

class Quantity:
  x=1
  y=2
  z=2

  def __index__(self):
    return self.x + self.y + self.z

quantity = Quantity() 
  
print('The binary equivalent string of ',quantity,' is: ',bin(quantity))