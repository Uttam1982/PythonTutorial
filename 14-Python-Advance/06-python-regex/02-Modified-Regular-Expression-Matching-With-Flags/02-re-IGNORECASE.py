# re.I
# re.IGNORECASE
#-------------------------------------------------------------------------------------------------
# Makes matching case insensitive.

# When IGNORECASE is in effect, character matching is case insensitive:
#-------------------------------------------------------------------------------------------------
import re

# Output : <re.Match object; span=(0, 3), match='aaa'>
print(re.search('a+','aaaAAA'))

# Output : <re.Match object; span=(3, 6), match='AAA'>
print(re.search('A+','aaaAAA'))


# Output : <re.Match object; span=(0, 6), match='aaaAAA'>
print(re.search('a+','aaaAAA',re.IGNORECASE))

# Output : <re.Match object; span=(0, 6), match='aaaAAA'>
print(re.search('A+','aaaAAA',re.I))

#-------------------------------------------------------------------------------------------------
# IGNORECASE affects alphabetic matching involving character classes as well:
#-------------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 1), match='a'>
print(re.search('[a-z]+','aEiOu')) # match='a'

# Output : <re.Match object; span=(0, 5), match='aEiOu'>
print(re.search('[a-z]+','aEiOu',re.IGNORECASE)) # match='aEiOu'