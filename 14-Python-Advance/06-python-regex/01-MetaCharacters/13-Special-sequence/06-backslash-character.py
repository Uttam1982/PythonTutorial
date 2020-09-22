#-------------------------------------------------------------------------------------------
# backslash (\)
#-------------------------------------------------------------------------------------------
# Removes the special meaning of a metacharacter.
#-------------------------------------------------------------------------------------------
# As you’ve just seen, the backslash character can introduce special character 
# classes like word, digit, and whitespace. 

# When it’s not serving either of these purposes, the backslash escapes metacharacters. 
# A metacharacter preceded by a backslash loses its special meaning and matches 
# the literal character instead.

#-------------------------------------------------------------------------------------------
import re

# Output: <re.Match object; span=(0, 1), match='a'>
print(re.search('.','abc.def'))

# Output: <re.Match object; span=(3, 4), match='.'>
print(re.search('\\.','abc.def'))

# So it isn’t a wildcard. It’s interpreted literally and matches the '.' 
# at index 3 of the search string.

#-------------------------------------------------------------------------------------------

s = r'foo\bar'
print(s)

#-------------------------------------------------------------------------------------------
# create a <regex> that will match the backslash between 'foo' and 'bar'. 
# The backslash is itself a special character in a regex, so to specify 
# a literal backslash, you need to escape it with another backslash
#-------------------------------------------------------------------------------------------

# Output: re.error: bad escape (end of pattern) at position 0

print(re.search('\\',s))

# Oops. What happened?
#-------------------------------------------------------------------------------------------
# The problem here is that the backslash escaping happens twice, 

# 1. first by the Python interpreter on the string literal and 
# 2. then again by the regex parser on the regex it receives.


# Here’s the sequence of events:

# The Python interpreter is the first to process the string literal '\\'. 
# It interprets that as an escaped backslash and passes only a single backslash to 
# re.search().

# The regex parser receives just a single backslash, which isn’t a meaningful regex, 
# so the messy error ensues.

#-------------------------------------------------------------------------------------------
s = r'foo\bar'

# Output : <re.Match object; span=(3, 4), match='\\'>
print(re.search('\\\\',s))

# The second, and probably cleaner, way to handle this 
# is to specify the <regex> using a raw string:


# Output : <re.Match object; span=(3, 4), match='\\'>
print(re.search(r'\\',s))
