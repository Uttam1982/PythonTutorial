#----------------------------------------------------------------------------------------------
# $
# \Z
#----------------------------------------------------------------------------------------------

# Anchor a match to the end of <string>.

#----------------------------------------------------------------------------------------------
# When the regex parser encounters $ or \Z, the parser’s current position must be at the end 
# of the search string for it to find a match. Whatever precedes $ or \Z must constitute the 
# end of the search string:
import re

# Output : <re.Match object; span=(3, 6), match='bar'>
print(re.search('bar$', 'foobar'))

# Output : None
print(re.search('bar$', 'barfoo'))


# Output : <re.Match object; span=(3, 6), match='bar'>
print(re.search('bar\\Z', 'foobar'))

# Output : None
print(re.search('bar\\Z', 'barfoo'))

print('*'*100)
#----------------------------------------------------------------------------------------------
# As a special case, $ (but not \Z) also matches just before a single newline 
# at the end of the search string:

# Output : <re.Match object; span=(3, 6), match='bar'>
print(re.search('bar$', 'foobar\n'))

# Output : None
print(re.search('bar\\Z', 'foobar\n'))

print('*'*100)
#----------------------------------------------------------------------------------------------
# $ and \Z behave slightly differently from each other in MULTILINE mode
#----------------------------------------------------------------------------------------------
s = "foo\nbar\nzoo"

# Output
# foo
# bar
# zoo
print(s)

# Output : None
print(re.search('foo$',s))
# Output : None
print(re.search('bar$',s))
# Output : <re.Match object; span=(8, 11), match='zoo'>
print(re.search('zoo$',s))

print('*'*100)

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo$',s, re.MULTILINE))
# Output : <re.Match object; span=(4, 7), match='bar'>
print(re.search('bar$',s,re.M))
# Output : <re.Match object; span=(8, 11), match='zoo'>
print(re.search('zoo$',s,re.M))

print('*'*100)
#----------------------------------------------------------------------------------------------

s = "foo\nbar\nzoo"

# Output : None
print(re.search('foo\\Z',s))
# Output : None
print(re.search('bar\\Z',s))
# Output : <re.Match object; span=(8, 11), match='zoo'>
print(re.search('zoo\\Z',s))

print('*'*100)

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo\\Z',s, re.MULTILINE))
# Output : <re.Match object; span=(4, 7), match='bar'>
print(re.search('bar\\Z',s,re.M))
# Output : <re.Match object; span=(8, 11), match='zoo'>
print(re.search('zoo\\Z',s,re.M))
