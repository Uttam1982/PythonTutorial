# What is Name in Python?

# Name (also called identifier) is simply a name given to objects. 
# Everything in Python is an object. 
# Name is a way to access the underlying object.

# We can get the address (in RAM) of some object through the built-in function id()

# ****************************************************************************************** 
# Note: You may get different values for the id

a = 2
b = 2
print('id(a) = ',id(a))     #1234
print('id(b) = ',id(b))     #1234
print('id(2) = ',id(2))     #1234

# Here, all refer to the same object 2, so they have the same id()

x = 2
print('Before id(x) = ',id(x)) #4567
x = x+1
print('After id(x) = ',id(x))  #6789
print('id(3) = ', id(3))       #6789
y=2
print('id(y) = ',id(y))        #4567


# This is efficient as Python does not have to create a new duplicate object. 
# This dynamic nature of name binding makes Python powerful; 
# a name could refer to any type of object.

a = 5
print('id(a) = ',id(a)) 
a = "Python"
print('id(a) = ',id(a)) 
a = [1,2,3]
print('id(a) = ',id(a)) 

# All these are valid and a will refer to three different types of objects in different instances.

# ****************************************************************************************** 

# Functions are objects too, so a name can refer to them as well.

def sayHello():
  print('Hello')

a = sayHello

print('variable a refer to a function')
a()
