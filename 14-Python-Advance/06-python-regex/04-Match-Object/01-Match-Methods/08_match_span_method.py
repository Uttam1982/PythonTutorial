# match.span([<grp>])
#--------------------------------------------------------------------------------------------

# Returns both the starting and ending indices of the match.

# match.span() returns both the starting and ending indices of the match as a tuple. 
# If you specified <grp>, then the return tuple applies to the given group:

#--------------------------------------------------------------------------------------------

import re

s = 'foo123bar456baz'

regex = r'(\d+)\D*(?P<num>\d+)'

m = re.search(regex,s)
# Output : <re.Match object; span=(3, 12), match='123bar456'>
print(m)

# Output : (3, 12)
print(m.span())

# ('123', '456')
print(m.groups())

# output : (3, 6)
print(m.span(1))

# output : (9, 12)
print(m.span('num'))

# The following are effectively equivalent:

# match.span(<grp>)
# (match.start(<grp>), match.end(<grp>))

# match.span() just provides a convenient way to obtain both match.start() 
# and match.end() in one method call.