#-------------------------------------------------------------------------------------
# $ - Dollar
#-------------------------------------------------------------------------------------
# The dollar symbol $ is used to check if a string ends with a certain character.

import re

pattern = "a$"
list_str = ['a','formula','cab']

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#-------------------------------------------------------------------------------------
