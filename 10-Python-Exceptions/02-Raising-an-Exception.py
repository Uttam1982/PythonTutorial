#--------------------------------------------------------------------------------
# Raising an Exception
#--------------------------------------------------------------------------------

# We can use raise to throw an exception if a condition occurs. 
# The statement can be complemented with a custom exception.

#--------------------------------------------------------------------------------

x = 10

if x > 5:
  # raise Exception('x should not exceed 5, The value of x is {}'.format(x))
  pass

# line 13, in <module>
    # raise Exception('x should not exceed 5, The value of x is {}'.format(x))
# Exception: x should not exceed 5, The value of x is 10

#--------------------------------------------------------------------------------

try:
  a = int(input("Enter a positive number: "))
  if a <= 0:
    raise ValueError("That is not a positive a number! ")
except ValueError as ve:
  print(ve)

