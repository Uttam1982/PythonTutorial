import re

# output: <re.Match object; span=(3, 6), match='123'>
print(re.search(r'\d+','foo123bar'))


re_obj = re.compile(r'\d+')

# There are two ways to use a compiled regular expression object. You can specify 


# 1. It as the first argument to the re module functions in place of <regex>:
# Output : <re.Match object; span=(3, 6), match='123'>
print(re.search(re_obj,'foo123bar'))


# 2. You can also invoke a method directly from a regular expression object:
# Output : <re.Match object; span=(3, 6), match='123'>
print(re_obj.search('foo123bar'))

#--------------------------------------------------------------------------------------------
# Using  IGNORECASE flag:
#--------------------------------------------------------------------------------------------

# output: <re.Match object; span=(3, 6), match='BAR'>
print(re.search('ba[rz]','FOOBARBAZ',re.IGNORECASE))


re_obj = re.compile('ba[rz]', re.I)

# There are two ways to use a compiled regular expression object. You can specify 


# 1. It as the first argument to the re module functions in place of <regex>:
# Output : <re.Match object; span=(3, 6), match='BAR'>
print(re.search(re_obj,'FOOBARBAZ'))


# 2. You can also invoke a method directly from a regular expression object:
# Output : <re.Match object; span=(3, 6), match='BAR'>
print(re_obj.search('FOOBARBAZ'))

#--------------------------------------------------------------------------------------------

