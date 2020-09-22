# \ - Backslash
#---------------------------------------------------------------------------------------
# Backlash \ is used to escape various characters including all metacharacters. 

# For example: '\$a' match if a string contains $ followed by a. 

# Here, $ is not interpreted by a RegEx engine in a special way.
# If you are unsure if a character has special meaning or not, 
# you can put \ in front of it. This makes sure the character is 
# not treated in a special way.

#---------------------------------------------------------------------------------------
import re

pattern = "\\$a"

test_str = ['ca','$a','$abcd','xy$abc','xyz\\$a']

result = [x for x in test_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------