#-------------------------------------------------------------------------------------
# re.subn(<regex>, <repl>, <string>, count=0, flags=0)
#-------------------------------------------------------------------------------------

# Returns a new string that results from performing replacements on a search 
# string and also returns the number of substitutions made.

# re.subn() is identical to re.sub(), except that re.subn() returns a two-tuple 
# consisting of the modified string and the number of substitutions made:

#-------------------------------------------------------------------------------------

import re

# Output : ('xxx.xxx.xxx.xxx', 4)
print(re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux'))

# Output : ('xxx.xxx.baz.qux', 2)
print(re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux',count= 2))

def f(match_obj):
  m = match_obj.group(0)
  if m.isdigit():
    return str(int(m) * 10)
  else:
    return m.upper()

# Output : ('FOO.100.BAR.200.BAZ.300', 6)
print(re.subn(r'\w+',f,'foo.10.bar.20.baz.30'))

# In all other respects, re.subn() behaves just like re.sub().