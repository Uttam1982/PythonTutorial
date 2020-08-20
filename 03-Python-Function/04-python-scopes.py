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




