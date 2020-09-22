# Capturing Groups
#-------------------------------------------------------------------------------------------
# Grouping isn’t the only useful purpose that grouping constructs serve. 
# Most (but not quite all) grouping constructs also capture the part of the 
# search string that matches the group. You can retrieve the captured portion 
# or refer to it later in several different ways.

#-------------------------------------------------------------------------------------------
# Remember the match object that re.search() returns? 

# There are two methods defined for a match object that provide access 
# to captured groups: 
# .groups() and .group().

#-------------------------------------------------------------------------------------------
# m.groups()
#-------------------------------------------------------------------------------------------
# Returns a tuple containing all the captured groups from a regex match.

# Consider this example:
import re

m = re.search('(\\w+),(\\w+),(\\w+)', 'foo,bar,quxx')
# Output : <re.Match object; span=(0, 12), match='foo,bar,quxx'>
print(m)

# Returns tuple containing all the captured matches in order: 
# Output: ('foo', 'bar', 'quxx')
print(m.groups())

# Notice that the tuple contains the tokens but not the commas 
# that appeared in the search string. That’s because the word characters 
# that make up the tokens are inside the grouping parentheses 
# but the commas aren’t. 

# The commas that you see between the returned tokens 
# are the standard delimiters used to separate values in a tuple.

#-------------------------------------------------------------------------------------------
# m.group(<n>)
#-------------------------------------------------------------------------------------------

# Returns a string containing the <n>th captured match.

# With one argument, .group() returns a single captured match. 

# Note that the arguments are one-based, not zero-based. 
# So, m.group(1) refers to the first captured match, 
# m.group(2) to the second, and so on:

#-------------------------------------------------------------------------------------------

m = re.search('(\\w+),(\\w+),(\\w+)', 'foo,bar,quxx')

# Output: ('foo', 'bar', 'quxx')
print(m.groups())

print(m.group(1)) # foo
print(m.group(2)) # bar
print(m.group(3)) # quxx


# Since the numbering of captured matches is 1-based, and 
# here isn’t any group numbered zero, 

# m.group(0) has a special meaning:

# foo,bar,quxx
print(m.group(0))

# foo,bar,quxx
print(m.group())

# m.group(0) returns the entire match, and m.group() does the same.

#-------------------------------------------------------------------------------------------
# m.group(<n1>, <n2>, ...)
#-------------------------------------------------------------------------------------------

# Returns a tuple containing the specified captured matches.

# With multiple arguments, .group() returns a tuple containing 
# the specified captured matches in the given order:

# Returns a tuple object
# Output : ('foo', 'bar', 'quxx')
print(m.groups())

# Returns a tuple object
# Output: ('bar', 'quxx')
print(m.group(2,3))

# Returns a tuple object
# Output: ('quxx', 'bar', 'foo')
print(m.group(3,2,1))

# This is just convenient shorthand
print((m.group(3),m.group(2),m.group(1)))

#-------------------------------------------------------------------------------------------