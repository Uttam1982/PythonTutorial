# re.X
# re.VERBOSE
#----------------------------------------------------------------------------------------------
# Allows inclusion of whitespace and comments within a regex.

# The VERBOSE flag specifies a few special behaviors:

# The regex parser ignores all whitespace unless it’s within a character class 
# or escaped with a backslash.

# If the regex contains a # character that isn’t contained within a character 
# class or escaped with a backslash, then the parser ignores it and all characters 
# to the right of it.

#----------------------------------------------------------------------------------------------

# Suppose you want to parse phone numbers that have the following format:

# Optional three-digit area code, in parentheses
# Optional whitespace
# Three-digit prefix
# Separator (either '-' or '.')
# Four-digit line number
# The following regex does the trick:
#----------------------------------------------------------------------------------------------
regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

import re

# Output : <re.Match object; span=(0, 13), match='(040)123-4567'>
print(re.search(regex,'(040)123-4567'))

# Output : <re.Match object; span=(0, 13), match='(040)123.4567'>
print(re.search(regex,'(040)123.4567'))

# Output : <re.Match object; span=(0, 8), match='123-4567'>
print(re.search(regex,'123-4567'))

# Output : <re.Match object; span=(0, 8), match='123.4567'>
print(re.search(regex,'123.4567'))

# Output : <re.Match object; span=(0, 14), match='(040) 123.4567'>
print(re.search(regex,'(040) 123.4567'))

#----------------------------------------------------------------------------------------------
# Using the VERBOSE flag, you can write the same regex in Python like this instead:
#----------------------------------------------------------------------------------------------

regex = r'''^             # Start of string
            (\(\d{3}\))?   # Optional area code
            \s*           # Optional whitespace
            \d{3}         # Three-digit prefix
            [-.]          # Separator character
            \d{4}         # Four-digit line number
            $             # Anchor at end of string
            '''

# Output : None
print(re.search(regex,'(712)123-4567'))

# Output : None
print(re.search(regex,'(712)123-4567', re.VERBOSE))

# Output : <re.Match object; span=(0, 13), match='(040)123.4567'>
print(re.search(regex,'(712)123.4567', re.VERBOSE))

# Output : <re.Match object; span=(0, 8), match='123-4567'>
print(re.search(regex,'123-4567', re.X))

# Output : <re.Match object; span=(0, 8), match='123.4567'>
print(re.search(regex,'123.4567', re.X))

# Output : <re.Match object; span=(0, 14), match='(040) 123.4567'>
print(re.search(regex,'(712) 123.4567', re.X))


#----------------------------------------------------------------------------------------------
# When using the VERBOSE flag, be mindful of whitespace that you do intend to be significant.
#----------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(0, 7), match='sam joe'>
print(re.search('sam joe','sam joe'))

# Output : None
print(re.search('sam joe','sam joe', re.VERBOSE))

# It doesn’t because the VERBOSE flag causes the parser to ignore the space character.

# Output : <re.Match object; span=(0, 7), match='sam joe'>
print(re.search('sam\\ joe','sam joe', re.VERBOSE))

# Output : None
print(re.search('sam[ ]joe','sam joe'))

# Output : <re.Match object; span=(0, 7), match='sam joe'>
print(re.search('sam[ ]joe','sam joe', re.VERBOSE))

# To make this match as expected, escape the space character 
# with a backslash or include it in a character class

#----------------------------------------------------------------------------------------------