# Example of Scope and Namespace in Python

def outer_function():
  y = 20
  def inner_function():
    z = 30
    print("z = ",z)
  
  inner_function()
  print("y = ",y)

x= 10
outer_function()
print("x = ",x)


# Here, the variable x is in the global namespace
# Variable y is in the local namespace of outer_function() 
# z is in the nested local namespace of inner_function()

# When we are in inner_function() 
# - c is local to us, b is nonlocal and a is global.
# - We can read as well as assign new values to c
# - but can only read b and a from inner_function().
# - If we try to assign as a value to b, a new variable b 
#   is created in the local namespace which is different than the nonlocal b. 
# - The same thing happens when we assign a value to a.
# - However, if we declare a as global, all the reference and assignment go to the global a. 
# - Similarly, if we want to rebind the variable b, it must be declared as nonlocal.


