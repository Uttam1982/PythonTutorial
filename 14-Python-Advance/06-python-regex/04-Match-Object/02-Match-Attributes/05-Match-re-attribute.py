#--------------------------------------------------------------------------------------------
# match.re
#--------------------------------------------------------------------------------------------
# Contains the regular expression object for the match.

# match.re contains the regular expression object that produced the match. 
# This is the same object you’d get if you passed the regex to re.compile():

#--------------------------------------------------------------------------------------------

import re

regex = r'(\w+),(\w+),(\w+)'

m1 = re.search(regex, 'foo,bar,baz')
# Output : re.Match object; span=(0, 11), match='foo,bar,baz'>
print(m1)

# re.compile('(\\w+),(\\w+),(\\w+)')
print(m1.re)


re_obj = re.compile(regex)
# e.compile('(\\w+),(\\w+),(\\w+)')
print(re_obj)

# True
print(re_obj is m1.re)

m2 = re_obj.search('qux,quux,corge')
# <re.Match object; span=(0, 14), match='qux,quux,corge'>
print(m2)

# re.compile('(\\w+),(\\w+),(\\w+)')
print(m2.re)

# True
print(re_obj is m1.re is m2.re)

# Once you have access to the regular expression object for the match, 
# all of that object’s attributes are available as well:

# Output : 3
print(m1.re.groups)

# output : (\w+),(\w+),(\w+)
print(m1.re.pattern)

# output : True
print(m1.re.pattern == regex)

# output : 32
print(m1.re.flags)


# You can also invoke any of the methods defined for a compiled regular expression 
# object on it:

m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

# Output : re.compile('(\\w+),(\\w+),(\\w+)')
print(m.re)

# Output : <re.Match object; span=(0, 17), match='quux,corge,grault'>
print(m.re.match('quux,corge,grault'))

# Here, .match() is invoked on m.re to perform another search using the same 
# regex but on a different search string.



