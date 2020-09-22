#-------------------------------------------------------------------------------------
# ? - Question Mark
#-------------------------------------------------------------------------------------
# The question mark symbol ? matches zero or one occurrence of the pattern left to it.

import re

pattern = 'ma?n'

strings = ['mn','man','maan','main','woman']

# maan : No Match
# main : No match (a is not followed by n)

result = [x for x in strings if re.search(pattern,x)]
print(result)

#-------------------------------------------------------------------------------------

