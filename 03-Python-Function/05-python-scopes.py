
# When we are in inner_function()
# ******************************************************************************************* 

# - c is local to us, b is nonlocal and a is global.
# - We can read as well as assign new values to c
# - but can only read b and a from inner_function().
# - If we try to assign as a value to b, a new variable b 
#   is created in the local namespace which is different than the nonlocal b. 
# - The same thing happens when we assign a value to a.
# - However, if we declare a as global, all the reference and assignment go to the global a. 
# - Similarly, if we want to rebind the variable b, it must be declared as nonlocal.

# *******************************************************************************************

# Example of Scope and Namespace in Python
def outer_fuction():
  x = 20               #non local variable w.r.t inner_function
  
  def inner_function():
    x = 30             #local variable w.r.t inner_function
    print("local variable w.r.t inner_function x = ",x)
  
  inner_function()
  print("non local variable w.r.t inner_function x = ",x)

x = 10                 #global variable
outer_fuction()
print("global variable x = ",x)

#In this program, three different variables x are defined in separate namespaces 
# and accessed accordingly.