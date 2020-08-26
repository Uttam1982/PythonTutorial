# Example 1: Create a Global Variable
x = 'global'

def foo():
  print("Inside function X= ",x)

foo()
print("Outside function X= ",x)

#********************************************************************************************

# What if you want to change the value of x inside a function?

x = 'global'

def boo():
  print("Inside function X= ",x * 2)

boo()
print("Outside function X= ",x)

#********************************************************************************************

# What if you want to change the value of x inside a function?

x = 'global'

def zoo():
  # x = x * 2      # Using variable 'x' before assignment
  print("Inside function X= ",x)

zoo()
print("Outside function X= ",x)

#********************************************************************************************
# To make this work, we use the global keyword. 

x = 'global'

def my_fun():
  global x
  x = x * 2      
  print("Inside function X= ",x)

my_fun()
print("Outside function X= ",x)