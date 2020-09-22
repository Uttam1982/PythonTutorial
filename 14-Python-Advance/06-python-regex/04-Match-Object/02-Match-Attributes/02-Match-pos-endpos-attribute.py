# match.pos

# match.endpos
#--------------------------------------------------------------------------------------------
# Contain the effective values of <pos> and <endpos> for the search.

# Remember that some methods, when invoked on a compiled regex, 
# accept optional <pos> and <endpos> arguments that limit the search 
# to a portion of the specified search string. These values are accessible 
# from the match object with the .pos and .endpos attributes

#--------------------------------------------------------------------------------------------
import re

re_obj = re.compile(r'\d+')


m = re_obj.search('foo123bar', 2, 7)

# Output : <re.Match object; span=(3, 6), match='123'>
print(m)

# Output : 2,7
print(m.pos, m.endpos)


# If the <pos> and <endpos> arguments aren’t included in the call, 
# either because they were omitted or because the function in question 
# doesn’t accept them, then the .pos and .endpos attributes effectively 
# indicate the start and end of the string:

#--------------------------------------------------------------------------------------------

re_obj = re.compile(r'\d+')

m = re_obj.search('foo123bar')

# Output : <re.Match object; span=(3, 6), match='123'>
print(m)

# Output : 0,9
print(m.pos, m.endpos)

#--------------------------------------------------------------------------------------------