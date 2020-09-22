# {m}
#--------------------------------------------------------------------------------------------
# Matches exactly m repetitions of the preceding regex.

# This is similar to * or +, but it specifies exactly how many times 
# the preceding regex must occur for a match to succeed:

#--------------------------------------------------------------------------------------------

import re

# Output : None
print(re.search('x-{3}x','x--x'))

# Output : <re.Match object; span=(0, 5), match='x---x'>
print(re.search('x-{3}x','x---x'))

# Output : None
print(re.search('x-{3}x','x----x'))

#--------------------------------------------------------------------------------------------
# {m,n}
#--------------------------------------------------------------------------------------------
# Matches any number of repetitions of the preceding regex from m to n, inclusive.

# Output : None
print(re.search('x-{2,4}x','x-x')) # 1 dash

# Output : <re.Match object; span=(0, 4), match='x--x'>
print(re.search('x-{2,4}x','x--x')) # 2 dashes

# Output : <re.Match object; span=(0, 5), match='x---x'>
print(re.search('x-{2,4}x','x---x')) # 3 dashes


# Output : <re.Match object; span=(0, 6), match='x----x'>
print(re.search('x-{2,4}x','x----x')) # 4 dashes  4 is inclusive

# Output : None
print(re.search('x-{2,4}x','x-----x')) # 5 dashes

#--------------------------------------------------------------------------------------------

# 1. <regex>{,n}	: Any number of repetitions of <regex> less than or equal to n	<regex>{0,n}

# 2. <regex>{m,}	Any number of repetitions of <regex> greater than or equal to m

# 3. <regex>{,}	Any number of repetitions of <regex>	<regex>{0,} <regex>*

# 4. If you omit all of m, n, and the comma, then the curly braces no longer function as 
#    metacharacters. {} matches just the literal string '{}':

#--------------------------------------------------------------------------------------------
# <regex>{,n}
#--------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 2), match='xx'>
print(re.search('x-{,4}x','xx')) # 0 dash

# Output : <re.Match object; span=(0, 3), match='x-x'>
print(re.search('x-{,4}x','x-x')) # 1 dash

# Output : <re.Match object; span=(0, 6), match='x----x'>
print(re.search('x-{,4}x','x----x')) # 4 dashes

# Output : None
print(re.search('x-{,4}x','x-----x')) # 5 dashes


#--------------------------------------------------------------------------------------------
# <regex>{m,}
#--------------------------------------------------------------------------------------------
# Output : None
print(re.search('x-{2,}x','x-x')) # 1 dashes

# Output : <re.Match object; span=(0, 4), match='x--x'>
print(re.search('x-{2,}x','x--x')) # 2 dashes

# Output : <re.Match object; span=(0, 6), match='x----x'>
print(re.search('x-{2,}x','x----x')) # 4 dashes

#--------------------------------------------------------------------------------------------
# <regex>{,}
#--------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 3), match='x-x'>
print(re.search('x-{,}x','x-x')) # 1 dashes

# Output : <re.Match object; span=(0, 4), match='x--x'>
print(re.search('x-{,}x','x--x')) # 2 dashes

# Output : <re.Match object; span=(0, 6), match='x----x'>
print(re.search('x-{,}x','x----x')) # 4 dashes

#--------------------------------------------------------------------------------------------

# If you omit all of m, n, and the comma, then the curly braces no longer function 
# as metacharacters. {} matches just the literal string '{}':

# Output : None
print(re.search('x-{}x','x--{}x'))

# Output : <re.Match object; span=(0, 5), match='x-{}x'>
print(re.search('x-{}x','x-{}x')) # matches just the literal string

#--------------------------------------------------------------------------------------------

# In fact, to have any special meaning, a sequence with curly braces must fit one of 
# the following patterns in which m and n are nonnegative integers:

# {m,n}
# {m,}
# {,n}
# {,}
# Otherwise, it matches literally:

# Output: <re.Match object; span=(0, 7), match='x{foo}y'>
print(re.search('x{foo}y','x{foo}y'))

# Output : <re.Match object; span=(0, 7), match='x{a:b}y'>
print(re.search('x{a:b}y','x{a:b}y'))

# Output : <re.Match object; span=(0, 9), match='x{1,2,3}y'>
print(re.search('x{1,2,3}y','x{1,2,3}y'))

# Output : <re.Match object; span=(0, 11), match='x{foo,bar}y'>
print(re.search('x{foo,bar}y','x{foo,bar}y'))

#--------------------------------------------------------------------------------------------
# {m,n}?
#--------------------------------------------------------------------------------------------
# The non-greedy (lazy) version of {m,n}.

# {m,n} will match as many characters as possible, and {m,n}? will match as few as possible:

# Output: <re.Match object; span=(0, 5), match='aaaaa'>
print(re.search('a{2,5}','aaaaa'))

# Output: <re.Match object; span=(0, 2), match='aa'>
print(re.search('a{2,5}?','aaaaa'))

# In this case, a{2,5} produces the longest possible match, so it matches five 'a' characters. 
# a{2,5}? produces the shortest match, so it matches two.

#--------------------------------------------------------------------------------------------