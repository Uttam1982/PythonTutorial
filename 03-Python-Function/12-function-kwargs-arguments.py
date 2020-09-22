# Types of arguments
# There may be several types of arguments which can be passed at the time of function call.

# 1. Required arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Variable-length arguments

#********************************************************************************************
# Keyword arguments
#********************************************************************************************

# Python provides the facility to pass the multiple keyword arguments which can be represented 
# as **kwargs. 
# 
# It is similar as the *args but it stores the argument in the dictionary format.

# This type of arguments is useful when we do not know the number of arguments in advance.

def basket(**kwargs):
  """
  pass the multiple keyword arguments
  """
  print("type of passed argument is ",type(kwargs)) 
  print(kwargs)

  for key, value in kwargs.items():
    print(f'key = {key}: value = {value}')


basket(fruit='Banana')
basket(fruit='Banana',vegetable='Carrot')

#---------------------------------------------------------------------------------









