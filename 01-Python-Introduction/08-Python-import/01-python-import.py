# Python Import
# When our program grows bigger, it is a good idea to break it into different modules.

# A module is a file containing Python definitions and statements. 
# Python modules have a filename and end with the extension .py.

# Definitions inside a module can be imported to another module or 
# the interactive interpreter in Python. 
# We use the import keyword to do this.

# ****************************************************************************************
# We can use the module in the following ways:
import math
print(math.pi)

# Now all the definitions inside math module are available in our scope. 

# ****************************************************************************************

# We can also import some specific attributes and functions only, using the from keyword. 
# For example:

from math import pi
print(pi)


# ****************************************************************************************
# While importing a module, Python looks at several places defined in sys.path. 
# It is a list of directory locations.

import sys
print(sys.path)

