# re.S
# re.DOTALL
#----------------------------------------------------------------------------------------------

# Causes the dot (.) metacharacter to match a newline.

# Remember that by default, the dot metacharacter matches any character 
# except the newline character. The DOTALL flag lifts this restriction:

#----------------------------------------------------------------------------------------------
import re

# Output : None
print(re.search('sam.ben','sam\nben'))

# Output : <re.Match object; span=(0, 7), match='sam\nben'>
print(re.search('sam.ben','sam\nben',re.DOTALL))

# Output : <re.Match object; span=(0, 7), match='sam\nben'>
print(re.search('sam.ben','sam\nben',re.S))