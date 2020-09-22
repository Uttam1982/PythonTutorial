#-------------------------------------------------------------------------------------------
# (?P<name><regex>)
#-------------------------------------------------------------------------------------------

# Creates a named captured group.

# you reference the matched group by its given symbolic <name> instead of by its number.

#-------------------------------------------------------------------------------------------
import re

m = re.search('(\\w+),(\\w+),(\\w+)','foo,boo,aux')
# Output : <re.Match object; span=(0, 11), match='foo,boo,aux'>
print(m)

# Output : foo
print(m.group(1))

# Output : foo
print(m.group(2))

# Output : foo
print(m.group(3))

print(m.groups())

print(m.group(1, 2, 3))

#-------------------------------------------------------------------------------------------
# The following effectively does the same thing except that the groups have the 
# symbolic names w1, w2, and w3: (?P<name><regex>)


m = re.search('(?P<w1>\\w+),(?P<w2>\\w+),(?P<w3>\\w+)','foo,boo,aux')
# output : <re.Match object; span=(0, 11), match='foo,boo,aux'>
print(m)

print(m.groups()) # ('foo', 'boo', 'aux')
print(m.group('w1')) # foo
print(m.group('w2')) # boo
print(m.group('w3')) # aux
print(m.group('w1','w2','w3')) # ('foo', 'boo', 'aux')
print(m.group(1,2,3)) # ('foo', 'boo', 'aux')

#-------------------------------------------------------------------------------------------
