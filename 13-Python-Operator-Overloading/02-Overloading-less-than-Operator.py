# Overloading Comparison Operators
#------------------------------------------------------------------------------------
# Python does not limit operator overloading to arithmetic operators only. 
# We can overload comparison operators as well.

# Suppose we wanted to implement the less than symbol < symbol in our Point class.

# Let us compare the magnitude of these points from the origin and return the result 
# for this purpose. 

# It can be implemented as follows.
#------------------------------------------------------------------------------------

class Point:
  def __init__(self, x,y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "{0},{1}".format(self.x,self.y)

  def __lt__(self,other):
    self_mag = (self.x ** 2) + (self.y ** 2)
    other_mag = (other.x ** 2) + (other.y ** 2)
    
    print(f"magnitude: ({self}) : {self_mag} ")
    print(f"magnitude: ({other}) : {other_mag} ")

    return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1, -1)

# use less than

print("p1<p2: ",p1<p2)
print("p2<p3: ",p2<p3)
print("p1<p3: ",p1<p3)





    