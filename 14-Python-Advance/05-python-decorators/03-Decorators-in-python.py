#----------------------------------------------------------------------------------------
# Decorators in Python
#----------------------------------------------------------------------------------------

# Basically, a decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
  def inner():
    print("I got decorated")
    func()
  
  return inner

def ordinary():
  print("I am ordinary")  

#----------------------------------------------------------------------------------------
# Generally, we decorate a function and reassign it as
ordinary()
ordinary = make_pretty(ordinary)
ordinary()
print("************************")

#----------------------------------------------------------------------------------------
# This is a common construct and for this reason, Python has a syntax to simplify this.
# We can use the @ symbol along with the name of the decorator function 
# and place it above the definition of the function to be decorated. 

# For example
@make_pretty
def someone_ordinary():
  print("Someone ordinary")

someone_ordinary()
#----------------------------------------------------------------------------------------
# is equivalent to
def some_ordinary():
  print("Someone ordinary")
some_ordinary = make_pretty(some_ordinary)


