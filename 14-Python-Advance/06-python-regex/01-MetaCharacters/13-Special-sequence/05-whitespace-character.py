#-------------------------------------------------------------------------------------------
# \s
# \S
#-------------------------------------------------------------------------------------------
# Match based on whether a character represents whitespace.

# \s matches any whitespace character:
# Note that, unlike the dot wildcard metacharacter, \s does match a newline character.
#-------------------------------------------------------------------------------------------

import re
# Output : <re.Match object; span=(3, 4), match=' '>
print(re.search('\\s','foo bar zoo'))

# Output : <re.Match object; span=(3, 4), match='\n'>
print(re.search('\\s','foo\nbar zoo')) # \s does match a newline character

#-------------------------------------------------------------------------------------------
# \S is the opposite of \s. It matches any character that isn’t whitespace:

# Output : <re.Match object; span=(3, 4), match='f'>
print(re.search('\\S',' \n foo \n '))


#-------------------------------------------------------------------------------------------
#  The character class sequences \w, \W, \d, \D, \s, and \S 
# can appear inside a square bracket []
#-------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(3, 4), match='3'>
print(re.search('[\\d\\w\\s]','---3---'))

# Output : <re.Match object; span=(3, 4), match='a'>
print(re.search('[\\d\\w\\s]','---a---'))

# Output : <re.Match object; span=(3, 4), match=' '>
print(re.search('[\\d\\w\\s]','--- ---'))


#-------------------------------------------------------------------------------------------

# In this case, [\d\w\s] matches any digit, word, or whitespace character. 
# And since \w includes \d, the same character class could also be expressed 
# slightly shorter as [\w\s].