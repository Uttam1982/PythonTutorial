# Python from...import statement
# When want to import specific names from a modules instead of import the whole module
# as a whole

# import only pi from math module

from math import pi
#Here, we imported only the pi attribute from the math module.

print("The value of pi is ",pi)

#import multiple attributes 
from math import pi, e
print("pi= ",pi)
print("e = ",e)

# import all names
from math import *

#Here, we have imported all the definitions from the math module. 
# This includes all names visible in our scope except those beginning 
# with an underscore(private definitions).

print("pi= ",pi)
print("e = ",e)
