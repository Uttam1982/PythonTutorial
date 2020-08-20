# Type Conversion
# The process of converting the value of one data type (integer, string, float, etc.) 
# to another data type is called type conversion. Python has two types of type conversion.

# 1. Implicit Type Conversion
# 2. Explicit Type Conversion


# 1. Implicit Type Conversion
# In Implicit type conversion, Python automatically converts one data type to 
# another data type. This process doesn't need any user involvement.

# Example 1: Converting integer to float
num_int = 5
num_float= 7.5
num_new = num_int + num_float

print("datatype of num_int:",type(num_int))
print("datatype of num_float:",type(num_float))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


# Example 2: Addition of string(higher) data type and integer(lower) datatype
num_int= 123
num_str='456'

num_new = num_int + num_str #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("datatype of num_int:",type(num_int))
print("datatype of num_str:",type(num_str))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new)) 

