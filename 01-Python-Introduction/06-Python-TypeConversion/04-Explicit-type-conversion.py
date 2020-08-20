# Explicit Type Conversion
# In Explicit Type Conversion, users convert the data type of an object to required data type. 
# We use the predefined functions like int(), float(), str(), etc 
# to perform explicit type conversion.

# This type of conversion is also called typecasting because the user casts (changes) 
# the data type of the objects.

# Example 3: Addition of string and integer using explicit conversion
num_int= 123
num_str='456'

num_new = num_int + int(num_str) 
print("datatype of num_int:",type(num_int))
print("datatype of num_str:",type(num_str))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))