class X:
  def display (self):
    print('X')

class Y:
  def display (self):
    print('Y')

class Z:
  def display (self):
    print('Z')

class A(X,Y):
  def display (self):
    print('A')

class B(Y,Z):
  def display (self):
    print('B')

class M(B,A,Z):
  pass

print(M.__mro__)

print(M.mro())

m = M()
m.display()
