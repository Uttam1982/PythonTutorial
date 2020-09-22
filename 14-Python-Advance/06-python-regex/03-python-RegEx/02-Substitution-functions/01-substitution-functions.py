# Substitution Functions
#-------------------------------------------------------------------------------------------

# Substitution functions replace portions of a search string that match a specified regex:

#-------------------------------------------------------------------------------------------
# Function	  Description
#-------------------------------------------------------------------------------------------
# re.sub()	  Scans a string for regex matches, replaces the matching portions of the 
#             string with the specified replacement string, and returns the result

# re.subn()	  Behaves just like re.sub() but also returns information regarding the 
#             number of substitutions made

#-------------------------------------------------------------------------------------------

# Both re.sub() and re.subn() create a new string with the specified substitutions 
# and return it. The original string remains unchanged. (Remember that strings are 
# immutable in Python, so it wouldn’t be possible for these functions to modify the 
# original string.)

