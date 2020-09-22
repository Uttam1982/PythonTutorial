# (?(<n>)<yes-regex>|<no-regex>)
# (?(<name>)<yes-regex>|<no-regex>)
#------------------------------------------------------------------------------------------------ 
# Specifies a conditional match.

# A conditional match matches against one of two specified regexes depending on 
# whether the given group exists:

# (?(<n>)<yes-regex>|<no-regex>) matches against <yes-regex> if a group numbered <n> exists. 
# Otherwise, it matches against <no-regex>.

# (?(<name>)<yes-regex>|<no-regex>) matches against <yes-regex> if a group named <name> exists. 
# Otherwise, it matches against <no-regex>.

#------------------------------------------------------------------------------------------------

# regex = r'^(###)?foo(?(1)bar|baz)'

# ^(###)? : 
# 1. indicates that the search string optionally begins with '###'. 
# 2. If it does, then the grouping parentheses around ### will create a group numbered 1. 
# Otherwise, no such group will exist.

# foo : The next portion, foo, literally matches the string 'foo'.

# (?(1)bar|baz) : matches against 'bar' if group 1 exists and 'baz' if it doesn’t.

#------------------------------------------------------------------------------------------------
import re


regex = r'^(###)?foo(?(1)bar|baz)'

m = re.search(regex,'###foobar')
# Output : <re.Match object; span=(0, 9), match='###foobar'>
print(m)

# The search string '###foobar' does start with '###', 
# so the parser creates a group numbered 1. 
# The conditional match is then against 'bar', which matches.

#------------------------------------------------------------------------------------------------
regex = r'^(###)?foo(?(1)bar|baz)'
m = re.search(regex,'###foobaz')
# Output : None
print(m)

# The search string '###foobar' does start with '###', 
# so the parser creates a group numbered 1. 
# The conditional match is then against 'bar', which doesn't match.

#------------------------------------------------------------------------------------------------
regex = r'^(###)?foo(?(1)bar|baz)'
m = re.search(regex,'foobar')
# Output : None
print(m)

# The search string 'foobar' doesn't start with '###', 
# so there isn’t a group numbered 1 
# The conditional match is then against 'baz', which doesn't match.

#------------------------------------------------------------------------------------------------
regex = r'^(###)?foo(?(1)bar|baz)'
m = re.search(regex,'foobaz')

# Output : <re.Match object; span=(0, 6), match='foobaz'>
print(m)

# The search string 'foobar' doesn't start with '###', 
# so there isn’t a group numbered 1 
# The conditional match is then against 'baz', which does matches.

#------------------------------------------------------------------------------------------------
# (?(<name>)<yes-regex>|<no-regex>) matches against <yes-regex> if a group named <name> exists. 
# Otherwise, it matches against <no-regex>.
#------------------------------------------------------------------------------------------------

# Here’s another conditional match using a named group instead of a numbered group:

#------------------------------------------------------------------------------------------------

regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

# ^	The start of the string
# (?P<ch>\W)	    : A single non-word character, captured in a group named ch
# (?P<ch>\W)?	    : Zero or one occurrences of the above
# foo             :	The literal string 'foo'
# (?(ch)(?P=ch)|) : The contents of the group named ch if it exists, 
#                   or the empty string if it doesn’t
# $	              : The end of the string

#------------------------------------------------------------------------------------------------
import re

regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(regex,'foo'))

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search(regex,'#foo#'))

# Output : <re.Match object; span=(0, 5), match='@foo@'>
print(re.search(regex,'@foo@'))

# Output : None
print(re.search(regex,'#foo'))

# Output : None
print(re.search(regex,'@foo'))


#------------------------------------------------------------------------------------------------













