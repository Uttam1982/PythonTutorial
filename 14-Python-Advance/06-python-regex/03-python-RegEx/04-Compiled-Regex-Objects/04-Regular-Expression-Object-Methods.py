# Regular Expression Object Methods
#--------------------------------------------------------------------------------------------
# A compiled regular expression object re_obj supports the following methods:

# Search methods
# re_obj.search(<string>[, <pos>[, <endpos>]])
# re_obj.match(<string>[, <pos>[, <endpos>]])
# re_obj.fullmatch(<string>[, <pos>[, <endpos>]])
# re_obj.findall(<string>[, <pos>[, <endpos>]])
# re_obj.finditer(<string>[, <pos>[, <endpos>]])

# Other methods
# re_obj.split(<string>, maxsplit=0)
# re_obj.sub(<repl>, <string>, count=0)
# re_obj.subn(<repl>, <string>, count=0)

#--------------------------------------------------------------------------------------------
import re

re_obj = re.compile(r'\d+')

s = 'foo123barbaz'

# Output : <re.Match object; span=(3, 6), match='123'>
print(re_obj.search(s))

# Output : <re.Match object; span=(3, 6), match='123'>
print(re_obj.search(s,0,6))


# Output : None
print(re_obj.search(s,6,9))

# Output : bar
print(s[6:9])

#--------------------------------------------------------------------------------------------

re_obj = re.compile('^bar')

s = 'foobarbaz'

# Output : <re.Match object; span=(3, 6), match='123'>
print(re_obj.search(s))

# Output : barbaz
print(s[3:])


# Output : None
print(re_obj.search(s,3,9))

# Here, even though 'bar' does occur at the start of the substring 
# beginning at character 3, it isn’t at the start of the entire string, 
# so the caret (^) anchor fails to match.

#--------------------------------------------------------------------------------------------