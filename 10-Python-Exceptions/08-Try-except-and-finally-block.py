#--------------------------------------------------------------------------------
# Try, except, and finally block
#--------------------------------------------------------------------------------
# The following code explains how error gets caught in the try block and 
# gets printed in the except block and then the finally block gets executed:

#--------------------------------------------------------------------------------

try:
  print(age)
except NameError as error:
  print(f"Error: {error}")
finally:
  print('finally block will always execute')


#--------------------------------------------------------------------------------


import sys

def linux_interaction():
  assert('darwin' in sys.platform),"Function can run only in mac(darwin) system"
  with open('file.log') as f:
    read_data = f.read()
    print(read_data)


try:
  linux_interaction()
  print("Try block executed successfully")
except AssertionError as error:
  print(error)
except FileNotFoundError as error:
  print(f"Error: {error}")
else:
  print("Else block executed ")
finally:
  print('finally block will always execute')
print("-------------------------------------")

#--------------------------------------------------------------------------------

def linux_interaction1():
  assert('linux' in sys.platform),"Function can run only in linux system"
  with open('file.log') as f:
    read_data = f.read()
    print(read_data)


try:
  linux_interaction1()
  print("Try block executed successfully")
except AssertionError as error:
  print(f"Error: {error}")
except FileNotFoundError as error:
  print(f"Error: {error}")
else:
  print("else block executed successfully")
finally:
  print('finally block will always execute')