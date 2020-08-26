# Reloading a module

# Now if our module changed during the course of the program, we would have to reload it
# Python provides a more efficient way of doing this. We can use the reload() function 
# inside the importlib module to reload a module. 

import importlib
import my_module
import my_module
importlib.reload(my_module)