# Overloading the + Operator
# 1. To overload the + operator, we will need to implement __add__() function in the class. 
# 2. With great power comes great responsibility. 
# 3. We can do whatever we like, inside this function. 
# 4. But it is more sensible to return a Point object of the coordinate sum.

class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return "{0},{1}".format(self.x,self.y)

  def __add__(self,other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x,y)

p1 = Point(3,4)
p2 = Point(5,6)

print(f"({p1}),({p2})")
print(p1+p2)

# What actually happens is that, when you use p1 + p2, 
# Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2). 
# After this, the addition operation is carried out the way we specified.

# https://www.programiz.com/python-programming/operator-overloading