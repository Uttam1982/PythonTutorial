#-----------------------------------------------------------------------------
# Chaining Decorators in Python
#-----------------------------------------------------------------------------
# Multiple decorators can be chained in Python.

# This is to say, a function can be decorated multiple times with 
# different (or same) decorators. 
# We simply place the decorators above the desired function.

#-----------------------------------------------------------------------------

def star(func):
  def inner(*args, **kwargs):
    print("*"*60)
    print(func)
    func(*args, **kwargs)
    print("*"*60)
  
  return inner

def hash(func):
  def inner(*args, **kwargs):
    print("#"*60)
    print(func)
    func(*args, **kwargs)
    print("#"*60)
  
  return inner

@star
@hash
def say_hello(msg):
  print(msg)

say_hello("Uttam")
print("-"*80)
#-----------------------------------------------------------------------------
# is equivalent to

def sayHello(msg):
    print(msg)
sayHello = star(hash(sayHello))

#-----------------------------------------------------------------------------

# The order in which we chain decorators matter. 


@hash
@star
def hello(msg):
  print(msg)

hello("Uttam")


#-----------------------------------------------------------------------------