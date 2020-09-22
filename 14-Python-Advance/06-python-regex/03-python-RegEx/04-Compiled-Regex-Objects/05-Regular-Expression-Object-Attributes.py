# Regular Expression Object Attributes
#--------------------------------------------------------------------------------------------

# The re module defines several useful attributes for a compiled regular 
# expression object:

#--------------------------------------------------------------------------------------------
# Attribute	          Meaning
#--------------------------------------------------------------------------------------------
# re_obj.flags	      Any <flags> that are in effect for the regex

# re_obj.groups	      The number of capturing groups in the regex

# re_obj.groupindex	  A dictionary mapping each symbolic group 
#                     name defined by the (?P<name>) construct (if any) to 
#                     the corresponding group number

# re_obj.pattern	    The <regex> pattern that produced this object

#--------------------------------------------------------------------------------------------

import re

re_obj = re_obj = re.compile(r'(?m)(\w+),(\w+)', re.I)

# Output : 42
print(re_obj.flags)

print(re.I|re.M|re.UNICODE)

# Note that .flags includes any flags specified as arguments to re.compile(), 
# any specified within the regex with the (?flags) metacharacter sequence, 
# and any that are in effect by default. In the regular expression object defined , 
# there are three flags defined:

# re.I: Specified as a <flags> value in the re.compile() call
# re.M: Specified as (?m) within the regex
# re.UNICODE: Enabled by default

#--------------------------------------------------------------------------------------------

# Output : 2
print(re_obj.groups)

# Output : (?m)(\w+),(\w+)
print(re_obj.pattern)

re_obj = re.compile(r'(?P<w1>),(?P<w2>)')

# Output : {'w1': 1, 'w2': 2}
print(re_obj.groupindex)

# Output : 1
print(re_obj.groupindex['w1'])

# Output : 2
print(re_obj.groupindex['w2'])

#--------------------------------------------------------------------------------------------