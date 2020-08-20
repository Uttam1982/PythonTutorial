
# When we are in inner_function()
# ******************************************************************************************* 

# - However, if we declare a as global, all the reference and assignment go to the global a. 
# - Similarly, if we want to rebind the variable b, it must be declared as nonlocal.

# *******************************************************************************************

# Example of Scope and Namespace in Python
def outer_fuction():
  global a               
  a = 20

  def inner_function():
    global a
    a = 30       
    print("inner_function a = ",a)
  
  inner_function()
  print("outer_function a = ",a)

a = 10                 #global variable
outer_fuction()
print("global variable a = ",a)

# Here, all references and assignments are to the global a due to the use of keyword global.