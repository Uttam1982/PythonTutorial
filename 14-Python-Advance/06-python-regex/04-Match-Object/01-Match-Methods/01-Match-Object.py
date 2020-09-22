# Match Object Methods and Attributes
#--------------------------------------------------------------------------------------------

# As you’ve seen, most functions and methods in the re module return a match object 
# when there’s a successful match. Because a match object is truthy, you can use it 
# in a conditional:

import re

m = re.search('bar','foo.bar.baz')

# Output : <re.Match object; span=(4, 7), match='bar'>
print(m)

# Output : True
print(bool(m))


if re.search('bar','foo.bar.baz'):
  print('Found a match')
else:
  print('No match found')

#--------------------------------------------------------------------------------------------
