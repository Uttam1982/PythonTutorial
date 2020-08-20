# Types of arguments
# There may be several types of arguments which can be passed at the time of function call.

# 1. Required arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Variable-length arguments

#*************************************************************************************************
# Variable-length arguments
#*************************************************************************************************
# Sometimes, we do not know in advance the number of arguments that will be passed into a function. 
# 
# Python allows us to handle this kind of situation through function calls with an arbitrary 
# number of arguments. 
# 
# When we call a function with some values, these values get assigned to the arguments according 
# to their position.
# 
# We define the variable-length argument using the *args (star) as *<variable - name >.
#
# Python provides us the flexibility to offer the comma-separated values which are internally 
# treated as tuples at the function call.

def greet(*names):
  """This function greets all
    the person in the names tuple."""
  
  print("type of passed argument is ",type(names))    
  
  # names is a tuple with arguments
  for  name in names:
    print(name)

greet('Sara','Joe','Harry','Sam')




