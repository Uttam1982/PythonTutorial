#---------------------------------------------------------------------------------------
# () - Group
#---------------------------------------------------------------------------------------

# Parentheses () is used to group sub-patterns. 
# For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

#---------------------------------------------------------------------------------------
import re

pattern ="(a|b|c)xz"

mylist = ['ab xz','abxz','axz' ,'cabxz']

result = [x for x in mylist if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------