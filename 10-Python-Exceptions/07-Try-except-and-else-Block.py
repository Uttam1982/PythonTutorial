#--------------------------------------------------------------------------------
# Try, except, and else block
#--------------------------------------------------------------------------------

# else block

# you can instruct a program to execute a certain block of code only in the absence of exceptions.
#--------------------------------------------------------------------------------
try:
  age = 21
  print(age)
except NameError as error:
  print(f"{error}")
else:
  print("Try block executed successfully\n")

#--------------------------------------------------------------------------------
# program to print the reciprocal of even numbers

try:
  num = int(input("Enter a number :"))
  assert num % 2 == 0
except:
  print("The number is not even\n")
else:
  r = 1/num
  print(f"reciprocal: {r} \n")


#--------------------------------------------------------------------------------
import sys

def linux_interaction():
  assert('darwin' in sys.platform),"Function can run only in mac(darwin) system"
  print("Inside the method")


try:
  linux_interaction()
except AssertionError as error:
  print(error)
else:
  print("Try block executed successfully")

#--------------------------------------------------------------------------------