#--------------------------------------------------------------------------------
# When do we have closures?
#--------------------------------------------------------------------------------

# 1. We must have a nested function (function inside a function).

# 2. The nested function must refer to a value defined in the enclosing function(outer)

# 3. The enclosing function(outer) must return the nested function.


#--------------------------------------------------------------------------------
# Defining a Closure Function
#--------------------------------------------------------------------------------

def show_msg(msg):
  # This is the outer enclosing function
  def show():
    # This is a nested function
    print(msg)

  # return the nested function
  return show

show_result = show_msg("Hello World")
print(show_result)
show_result()

#--------------------------------------------------------------------------------
# The show_msg() function was called with the string "Hello world" 
# and the returned function was bound to the name show_result. 
# On calling show_result(), the message was still remembered although 
# we had already finished executing the show_msg() function.

# This technique by which some data ("Hello World" in this case) 
# gets attached to the code is called closure in Python.

#--------------------------------------------------------------------------------

# This value in the enclosing scope is remembered even when the variable 
# goes out of scope or the function itself is removed from the current namespace.

del show_msg
print("after deleting show_msg method")
print(show_result)
show_result()

# NameError: name 'show_msg' is not defined
show_msg("Hello World")

#--------------------------------------------------------------------------------

