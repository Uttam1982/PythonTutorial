#----------------------------------------------------------------------------------------
# dot (.)
#----------------------------------------------------------------------------------------

# Specifies a wildcard.
# The . metacharacter matches any single character except a newline:

#----------------------------------------------------------------------------------------
import re
#output: <re.Match object; span=(0, 7), match='foozbar'>
print(re.search('foo.bar','foozbar'))

#output: None
print(re.search('foo.bar','foobar'))

#output: None
print(re.search('foo.bar','foo\nbar')) #dot (.) ignore \n new line character

