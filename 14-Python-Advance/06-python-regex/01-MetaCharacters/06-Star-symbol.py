#-------------------------------------------------------------------------------------
# * - Star
#-------------------------------------------------------------------------------------

# The star symbol * matches zero or more occurrences of the pattern left to it.

#-------------------------------------------------------------------------------------

import re

pattern = 'ma*n'

strings = ['mn','man','maan','main','woman']

# main : 	No match (a is not followed by n)

result = [x for x in strings if re.search(pattern,x)]
print(result)
