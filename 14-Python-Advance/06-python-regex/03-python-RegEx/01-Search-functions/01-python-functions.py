# The available regex functions in the Python re module fall into the following three categories:

# Searching functions
# Substitution functions
# Utility functions

# The following sections explain these functions in more detail.
#-----------------------------------------------------------------------------------------------
# 1. Searching Functions
#-----------------------------------------------------------------------------------------------

# Searching functions scan a search string for one or more matches of the specified regex:

#-----------------------------------------------------------------------------------------------
# Function	        Description
#-----------------------------------------------------------------------------------------------
# re.search()	      Scans a string for a regex match
# re.match()	      Looks for a regex match at the beginning of a string
# re.fullmatch()	  Looks for a regex match on an entire string
# re.findall()	    Returns a list of all regex matches in a string
# re.finditer()	    Returns an iterator that yields regex matches from a string

#-----------------------------------------------------------------------------------------------
# 2. Substitution Functions
#-----------------------------------------------------------------------------------------------

# Substitution functions replace portions of a search string that match a specified regex:

#-----------------------------------------------------------------------------------------------
# Function	  Description
#-----------------------------------------------------------------------------------------------
# re.sub()	  Scans a string for regex matches, replaces the matching portions of the 
#             string with the specified replacement string, and returns the result

# re.subn()	  Behaves just like re.sub() but also returns information regarding the 
#             number of substitutions made

#-----------------------------------------------------------------------------------------------
# 3. Utility Functions
#-----------------------------------------------------------------------------------------------

# There are two remaining regex functions in the Python re module that you’ve yet to cover:

#-----------------------------------------------------------------------------------------------
# Function	        Description
#-----------------------------------------------------------------------------------------------

# re.split()	      Splits a string into substrings using a regex as a delimiter
# re.escape()	      Escapes characters in a regex

#-------------------------------------------------------------------------------------------
# 4. Flags
#-------------------------------------------------------------------------------------------

# re.I	re.IGNORECASE	: Makes matching of alphabetic characters case-insensitive
# re.M	re.MULTILINE	: Causes start-of-string and end-of-string anchors to match embedded newlines
# re.S	re.DOTALL	    : Causes the dot metacharacter to match a newline
# re.X	re.VERBOSE	  : Allows inclusion of whitespace and comments within a regular expression
# ----	re.DEBUG	    : Causes the regex parser to display debugging information to the console
# re.A	re.ASCII	    : Specifies ASCII encoding for character classification
# re.U	re.UNICODE	  : Specifies Unicode encoding for character classification
# re.L  re.LOCALE	    : Specifies encoding for character classification based on the current locale

#-------------------------------------------------------------------------------------------
# 5. Compiled regular expression objects support the following methods and attributes:
#-------------------------------------------------------------------------------------------
# 1. Pattern.search(string[, pos[, endpos]])
# 2. Pattern.match(string[, pos[, endpos]])
# 3. Pattern.fullmatch(string[, pos[, endpos]])

# New in version 3.4.
# 4. Pattern.split(string, maxsplit=0)
# 5. Pattern.findall(string[, pos[, endpos]])
# 6. Pattern.finditer(string[, pos[, endpos]])
# 7. Pattern.sub(repl, string, count=0)
# 8. Pattern.subn(repl, string, count=0)

#-------------------------------------------------------------------------------------------
# 6.Match Objects
#-------------------------------------------------------------------------------------------
# 1. Match.expand(template)
# 2. Match.group([group1, ...])

# 3.Match.__getitem__(g)

# New in version 3.6.
# 4. Match.groups(default=None)
# 5. Match.groupdict(default=None)
# 6. Match.start([group])
# 7. Match.end([group])
# 8. Match.span([group])

# 9. Match.pos
# 10. Match.endpos
# 11. Match.lastindex
# 12. Match.lastgroup
# 13. Match.re
# 14. Match.string
#-------------------------------------------------------------------------------------------