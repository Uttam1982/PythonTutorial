# re.A
# re.ASCII
# re.U
# re.UNICODE
# re.L
# re.LOCALE
#----------------------------------------------------------------------------------------------
# Specify the character encoding used for parsing of special regex character classes.

# re.U and re.UNICODE specify Unicode encoding. 
# Unicode is the default, so these flags are superfluous. 
# They’re mainly supported for backward compatibility.

# re.A and re.ASCII force a determination based on ASCII encoding. 
# If you happen to be operating in English, then this is happening anyway, 
# so the flag won’t affect whether or not a match is found.

# re.L and re.LOCALE make the determination based on the current locale. 
# Locale is an outdated concept and isn’t considered reliable. 
# Except in rare circumstances, you’re not likely to need it.

#----------------------------------------------------------------------------------------------

s = '\u0967\u096a\u096c'
# Output : १४६
print(s)

import re

# <re.Match object; span=(0, 3), match='१४६'>
print(re.search(r'\d+',s))

# <re.Match object; span=(0, 3), match='१४६'>
print(re.search(r'\d+',s, re.UNICODE))


s = 'sch\u00f6n'
print(s)
# Output : <re.Match object; span=(0, 3), match='sch'>
print(re.search(r'\w+',s, re.ASCII))

# Output: <re.Match object; span=(0, 5), match='schön'>
print(re.search(r'\w+',s, re.UNICODE))

# Output: <re.Match object; span=(0, 5), match='schön'>
print(re.search(r'\w+',s))

#----------------------------------------------------------------------------------------------

