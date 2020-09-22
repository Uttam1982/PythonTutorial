# match.lastgroup
#--------------------------------------------------------------------------------------------
# Contains the name of the last captured group.

# If the last captured group originates from the (?P<name><regex>) 
# metacharacter sequence, then match.lastgroup returns the name of that group:

#--------------------------------------------------------------------------------------------
import re

s = 'foo123bar456baz'

m = re.search(r'(?P<n1>\d+)\D*(?P<n2>\d+)', s)

# Output : ('123', '456')
print(m.groups())

# Output : 123
print(m.group('n1'))

# Output : 456
print(m.group('n2'))

# Output : n2
print(m.lastgroup)

# match.lastgroup returns None if the last captured group isn’t a named group:

#--------------------------------------------------------------------------------------------
s = 'foo123bar456baz'

m = re.search(r'(?P<n1>\d+)\D*(\d+)', s)

# Output : ('123', '456')
print(m.groups())

# Output : None
print(m.lastgroup)

# As shown above, this can be either because the last captured group isn’t a 
# named group or because there were no captured groups at all.

#--------------------------------------------------------------------------------------------
