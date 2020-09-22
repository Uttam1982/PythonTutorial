# Most of the functions in the re module take an optional <flags> argument. 
# This includes the function you’re now very familiar with, re.search().

# re.search(<regex>, <string>, <flags>)

# Scans a string for a regex match, applying the specified modifier <flags>.

# Flags modify regex parsing behavior, allowing you to refine your pattern matching even further.
#------------------------------------------------------------------------------------------------- 
# Short Name	Long Name	      Effect
#-------------------------------------------------------------------------------------------------
# re.I	      re.IGNORECASE	  Makes matching of alphabetic characters case-insensitive
# re.M	      re.MULTILINE	  Causes start-of-string and end-of-string anchors to match 
#                             embedded newlines
# re.S	      re.DOTALL	      Causes the dot metacharacter to match a newline
# re.X	      re.VERBOSE	    Allows inclusion of whitespace and comments within a 
#                             regular expression
# ----	      re.DEBUG	      Causes the regex parser to display debugging information 
#                             to the console
# re.A	      re.ASCII	      Specifies ASCII encoding for character classification
# re.U	      re.UNICODE	    Specifies Unicode encoding for character classification
# re.L        re.LOCALE	      Specifies encoding for character classification based on 
#                             the current locale

#-------------------------------------------------------------------------------------------------