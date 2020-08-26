# Python Module Search Path
# While importing a module, Python looks at several places. 
# Interpreter first looks for a built-in module. 
# Then(if built-in module not found), Python looks into a list of 
# directories defined in sys.path. 
# 
# The search is in this order.
# 1. The current directory.
# 2. PYTHONPATH (an environment variable with a list of directories).
# 3. The installation-dependent default directory.

import sys
print(sys.path)