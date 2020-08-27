# How to delete a string?

# 1. We cannot delete or remove characters from a string. 
# 2. But deleting the string entirely is possible using the del keyword.

my_string = "Python"

# We cannot delete or remove characters from a string. 

# TypeError: 'str' object doesn't support item deletion
# del my_string[0]

# deleting the string entirely is possible using the del keyword.

del my_string

# NameError: name 'my_string' is not defined
print(my_string)

