# The dir() built-in function
# We can use the dir() function to find out names that are defined inside a module.

import example
print("dir(example): ",dir(example))

print("example.__doc__ : ",example.__doc__)
print("example.__file__: ",example.__file__)
print("example.__name__: ",example.__name__)

print("example.__package__: ",example.__package__)