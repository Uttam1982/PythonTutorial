# Nonlocal Variables
# Nonlocal variables are used in nested functions whose local scope is not defined. 
# This means that the variable can be neither in the local nor the global scope.

#*************************************************************************************
# create a non-local variable

def outer():
  global z
  x = 'local'

  def inner():
    nonlocal x
    x = 'non-local'
    y= 'local'
    print('inner x',x)
    print('inner y',y)
  
  inner()
  print('outer x',x)

outer()
print("******************")


#*************************************************************************************
# create a global, non-local and local variable

x = 'global'

def outer_fun():
  global x
  x = 'global-changed'
  y = 'local'

  def inner_fun():
    nonlocal y
    y = 'non-local'
    z= 'local'
    
    print('inner x: ',x)
    print('inner y: ',y)
    print('inner z: ',z)
  
  inner_fun()
  print('outer x: ',x)
  print('outer y: ',y)

print('before x: ',x)
outer_fun()
print('after x: ',x)