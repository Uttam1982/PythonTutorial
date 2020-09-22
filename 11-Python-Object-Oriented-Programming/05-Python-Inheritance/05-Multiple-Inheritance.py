class A:
  def msg(self):
    print("Hello")

class B:
  def msg(self):
    print("Welcome")

class C(A, B):
  pass

# __mro__ attribute
print(C.__mro__)

# mro() method.
print(C.mro())
c = C()
c.msg()

# This order is also called linearization of C class and 
# the set of rules used to find this order is called 
# Method Resolution Order (MRO).
