# Local Variables
# A variable declared inside the function's body or in the local scope is known 
# as a local variable.

# Example : Accessing local variable outside the scope
def my_fun():
  y = 'local'
  print("inside function y = ",y)

my_fun()
# print("outside function y = ",y) #Undefined variable 'y'


# Example : Using Global and Local variables in the same code
x = 'global'
def func1():
  global x
  x = x * 2
  y = "local"
  print('global variable: ', x)
  print('local variable: ',y)

func1()

# Example : Global variable and Local variable with same name

x = 5

def func2():
  x = 10
  print('local x :',x)

func2()
print('global x :',x)

