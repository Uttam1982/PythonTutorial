# match.groupdict(default=None)
#--------------------------------------------------------------------------------------------

# Returns a dictionary of named captured groups.

# match.groupdict() returns a dictionary of all named groups captured with the 
# (?P<name><regex>) metacharacter sequence. The dictionary keys are the group 
# names and the dictionary values are the corresponding group values:

#--------------------------------------------------------------------------------------------
import re

regex = r'foo,(?P<w1>\w+),(?P<w2>\w+),qux'
s = 'foo,bar,baz,qux'

m = re.search(regex,s)

# Output : <re.Match object; span=(0, 15), match='foo,bar,baz,qux'>
print(m)

# Output : {'w1': 'bar', 'w2': 'baz'}
print(m.groupdict())

# Output : baz
print(m.groupdict()['w2'])

#--------------------------------------------------------------------------------------------
# As with .groups(), for .groupdict() the default argument determines 
# the return value for nonparticipating groups:
regex = r'foo,(?P<w1>\w+),(?P<w2>\w+)?,qux'
s = 'foo,bar,,qux'

m = re.search(regex,s)

# Output : {'w1': 'bar', 'w2': None}
print(m.groupdict())

# Output : {'w1': 'bar', 'w2': '----'}
print(m.groupdict(default='----'))

#--------------------------------------------------------------------------------------------
# Again, the final group (?P<w2>\w+) doesn’t participate in the overall match 
# because of the question mark (?) metacharacter. By default, m.groupdict() 
# returns None for this group, but you can change it with the default argument.