# Reloading a module
# The Python interpreter imports a module only once during a session. 
# This makes things more efficient.

import my_module
import my_module
import my_module

#run the file and check the output

# Now if our module changed during the course of the program, we would have to reload it
# Python provides a more efficient way of doing this. We can use the reload() function 
# inside the imp module to reload a module. 

import imp
import my_module
imp.reload(my_module)