# Lookahead and Lookbehind Assertions

# Lookahead and lookbehind assertions determine the success or failure of 
# a regex match in Python based on what is just behind (to the left) or ahead 
# (to the right) of the parser’s current position in the search string.

#------------------------------------------------------------------------------------------------
# (?=<lookahead_regex>)
#------------------------------------------------------------------------------------------------
# Creates a positive lookahead assertion.

# (?=<lookahead_regex>) asserts that what follows the regex parser’s current 
# position must match <lookahead_regex>:

#------------------------------------------------------------------------------------------------
import re

# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo(?=[a-z])','foobar'))

# The lookahead assertion (?=[a-z]) specifies that what follows 'foo' 
# must be a lowercase alphabetic character. In this case, 
# it’s the character 'b', so a match is found.

# Output : None
print(re.search('foo(?=[a-z])','foo123'))

# the lookahead fails. The next character after 'foo' is '1', so there isn’t a match:

#------------------------------------------------------------------------------------------------

# Take another look at the first example:
# Output : <re.Match object; span=(0, 3), match='foo'>
print(re.search('foo(?=[a-z])','foobar'))

# The regex parser looks ahead only to the 'b' that follows 'foo' 
# but doesn’t pass over it yet. You can tell that 'b' isn’t considered 
# part of the match because the match object displays match='foo'.

#------------------------------------------------------------------------------------------------
# without lookahead
# Compare that to a similar example that uses grouping parentheses without a lookahead
#------------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(0, 4), match='foob'>
print(re.search('foo([a-z])','foobar'))

# This time, the regex consumes the 'b', and it becomes a part of the eventual match.

#------------------------------------------------------------------------------------------------
# illustrating how a lookahead differs from a conventional regex
#------------------------------------------------------------------------------------------------

m = re.search('foo(?=[a-z])(?P<ch>.)','foobar')

# Output : 'b'
print(m.group('ch'))

# 1. The first portion of the regex, foo, matches and consumes 'foo' 
#    from the search string 'foobar'.

# 2. The next portion, (?=[a-z]), is a lookahead that matches 'b', 
#    but the parser doesn’t advance past the 'b'.

# 3. Lastly, (?P<ch>.) matches the next single character available, which is 'b', 
#    and captures it in a group named ch.

# 4. The m.group('ch') call confirms that the group named ch contains 'b'.



m = re.search('foo([a-z])(?P<ch>.)','foobar')
# Output: 'a'
print(m.group('ch'))

# 1. As in the first example, the first portion of the regex, foo, 
#    matches and consumes 'foo' from the search string 'foobar'.

# 2. The next portion, ([a-z]), matches and consumes 'b', and the parser advances past 'b'.

# 3. Lastly, (?P<ch>.) matches the next single character available, which is now 'a'.

# 4. m.group('ch') confirms that, in this case, the group named ch contains 'a'.