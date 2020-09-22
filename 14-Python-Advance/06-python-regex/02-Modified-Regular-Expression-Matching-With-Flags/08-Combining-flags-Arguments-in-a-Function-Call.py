# Combining <flags> Arguments in a Function Call
#----------------------------------------------------------------------------------------------

# Flag values are defined so that you can combine them using the bitwise OR (|) operator. 
# This allows you to specify several flags in a single function call:

#----------------------------------------------------------------------------------------------

import re

# Output: <re.Match object; span=(4, 7), match='BAR'>
print(re.search('^bar','FOO\nBAR\nBAZ', re.I|re.M))

# This re.search() call uses bitwise OR to specify 
# both the IGNORECASE and MULTILINE flags at once.

#----------------------------------------------------------------------------------------------