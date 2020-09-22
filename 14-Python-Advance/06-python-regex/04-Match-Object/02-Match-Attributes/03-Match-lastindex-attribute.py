# match.lastindex
#--------------------------------------------------------------------------------------------

# Contains the index of the last captured group.
# match.lastindex is equal to the integer index of the last captured group:

#--------------------------------------------------------------------------------------------
import re

regex = r'(\w+),(\w+),(\w+)'

s = 'foo,bar,baz'

m = re.search(regex, s)

# Output : <re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m)

print(m.groups())
# 3
print(m.lastindex)

# baz
print(m[m.lastindex])

#--------------------------------------------------------------------------------------------
m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')

# ('foo', 'bar', None)
print(m.groups())

# 2 
print(m.lastindex)


# In the first example, the third group, which is optional because 
# of the question mark (?) metacharacter, does participate in the match. 

#--------------------------------------------------------------------------------------------

# There’s a subtle point to be aware of regarding .lastindex. 
# It isn’t always the case that the last group to match is also the last group 
# encountered syntactically. The Python documentation gives this example:

m = re.match('((a)(b))', 'ab')

# Output : ('ab', 'a', 'b')
print(m.groups())

# 1
print(m.lastindex)

# ab
print(m[m.lastindex])


# The outermost group is ((a)(b)), which matches 'ab'. 
# This is the first group the parser encounters, so it becomes group 1. 
# But it’s also the last group to match, which is why m.lastindex is 1.

# The second and third groups the parser recognizes are (a) and (b). 
# These are groups 2 and 3, but they match before group 1 does.

#--------------------------------------------------------------------------------------------


