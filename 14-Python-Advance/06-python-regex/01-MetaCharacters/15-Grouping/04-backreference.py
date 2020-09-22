#-------------------------------------------------------------------------------------------
# Backreferences
#-------------------------------------------------------------------------------------------
# You can match a previously captured group later within the same regex 
# using a special metacharacter sequence called a backreference.

#-------------------------------------------------------------------------------------------
# \<n>
#-------------------------------------------------------------------------------------------
# Matches the contents of a previously captured group.

# Within a regex in Python, the sequence \<n>, 
# where <n> is an integer from 1 to 99, matches the contents of the <n>th captured group.

# Here’s a regex that matches a word, followed by a comma, followed by the same word again:

#-------------------------------------------------------------------------------------------
import re
regex = r'(\w+),\1'

m = re.search(regex,'foo,foo')
# Output: <re.Match object; span=(0, 7), match='foo,foo'>
print(m)
# Output : foo
print(m.group(1))

m = re.search(regex,'foo,boo')
# Output : None
print(m)

# In the first example, (\w+) matches the first instance of the string 'foo' 
# and saves it as the first captured group. The comma matches literally. 
# Then \1 is a backreference to the first captured group and matches 'foo' again.


# The last example, on line 15, doesn’t have a match because what comes before 
# the comma isn’t the same as what comes after it, so the \1 backreference doesn’t match.

#-------------------------------------------------------------------------------------------
# Note: Any time you use a regex in Python with a numbered backreference, 
# it’s a good idea to specify it as a raw string. Otherwise, the interpreter 
# may confuse the backreference with an octal value.

# Output : None
print(re.search('([a-z])#\1','b#b'))

# The regex ([a-z])#\1 matches a lowercase letter, followed by '#', 
# followed by the same lowercase letter. The string in this case is 'b#b', 
# which should match. But the match fails because Python misinterprets 
# the backreference \1 as the character whose octal value is one:

print(oct(ord('\1')))

# Output: <re.Match object; span=(0, 3), match='b#b'>
print(re.search(r'([a-z])#\1','b#b'))


#-------------------------------------------------------------------------------------------