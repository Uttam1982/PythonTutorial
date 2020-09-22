#--------------------------------------------------------------------------------------------
# Decorators in Python
#--------------------------------------------------------------------------------------------

# Python has an interesting feature called decorators to add functionality to 
# an existing code.

# This is also called metaprogramming because a part of the program tries to 
# modify another part of the program at compile time.

#--------------------------------------------------------------------------------------------
# Prerequisites for learning decorators
#--------------------------------------------------------------------------------------------
# 1. Everything in Python (Yes! Even classes), are objects. 
# 2. Names that we define are simply identifiers bound to these objects. 
# 3. Functions are no exceptions, they are objects too (with attributes). 
# 4. Various different names can be bound to the same function object.
# 5. Functions can be passed as arguments to another function.
#--------------------------------------------------------------------------------------------

def first(msg):
  print(msg)

print("function object first: ",first) # <function first at 0x7f8f5e443710>
first("uttam")

second = first
print("function object second: ",second) # <function first at 0x7f8f5e443710>
second("uttam")

# Here, the names first and second refer to the same function object.

#--------------------------------------------------------------------------------------------
# Functions can be passed as arguments to another function.

def inc(x):
  return x + 1

def dec(x):
  return x - 1

def operate(func, x):
  result = func(x)
  return result

print("calling inc function: ",operate(inc,3))
print("calling dec function: ",operate(dec,3))

#--------------------------------------------------------------------------------------------
# Furthermore, a function can return another function 

def show_msg(msg):
  def show():
    print(msg)
  
  print("function object show: ",show)  
  return show

show_result = show_msg('uttam')
print("function object returned: ",show_result)
show_result()

# here show and show_result refers to the same function object
