# | - Alternation
#---------------------------------------------------------------------------------------

# Vertical bar | is used for alternation (or operator).

#---------------------------------------------------------------------------------------
import re

pattern ='a|b'

list_str = ['cde','ade','acdbea']

# cde	    : No match
# ade	    : 1 match (match at ade)
# acdbea  :	3 matches (at acdbea)

result = [x for x in list_str if re.search(pattern,x)]
print(result)

#---------------------------------------------------------------------------------------

