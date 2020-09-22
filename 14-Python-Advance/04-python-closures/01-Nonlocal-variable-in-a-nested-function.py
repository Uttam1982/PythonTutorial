#-----------------------------------------------------------------------------------------
# Python Closures
#-----------------------------------------------------------------------------------------

# Before getting into what a closure is, we have to first understand 
# what a nested function and nonlocal variable is.

# A function defined inside another function is called a nested function. 
# Nested functions can access variables of the enclosing scope.

# In Python, these non-local variables are read-only by default and we must 
# declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

#-----------------------------------------------------------------------------------------
# Example of a nested function accessing a non-local variable.

def show_msg(msg):
  # This is the outer enclosing function
  def show():
    # This is the nested function
    print(msg)
  
  show()
# We execute the function
# Output: Hello World
show_msg("Hello World")