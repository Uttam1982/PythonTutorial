# match.string

# Contains the search string for a match.

# match.string contains the search string that is the target of the match:

import re

m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

# Output : foo,bar,baz
print(m.string)


re_obj = re.compile(r'(\w+),(\w+),(\w+)')
m = re_obj.search('foo,bar,baz')

# Output : foo,bar,baz
print(m.string)
