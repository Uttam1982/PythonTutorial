# Why Bother Compiling a Regex?

# If you use a particular regex in your Python code frequently, 
# then precompiling allows you to separate out the regex definition from its uses. 
# This enhances modularity. Consider this example:

# Without compiled object

import re

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

# Output : None
print(re.search(r'\d+', s1))

# Output: <re.Match object; span=(3, 6), match='123'>
print(re.search(r'\d+',s2))

# Output : <re.Match object; span=(3, 5), match='99'>
print(re.search(r'\d+',s3))

# Output : None
print(re.search(r'\d+',s4))

# Here, the regex \d+ appears several times. If, in the course of maintaining this code, 
# you decide you need a different regex, then you’ll need to change it in each location. 
# That’s not so bad in this small example because the uses are close to one another. 
# But in a larger application, they might be widely scattered and difficult to track down.

# The following is more modular and more maintainable:



#--------------------------------------------------------------------------------------------

# With compiled object

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

re_obj = re.compile(r'\d+')

# Output : None
print(re_obj.search(s1))

# Output: <re.Match object; span=(3, 6), match='123'>
print(re_obj.search(s2))

# Output : <re.Match object; span=(3, 5), match='99'>
print(re_obj.search(s3))

# Output : None
print(re_obj.search(s4))

#--------------------------------------------------------------------------------------------

# Then again, you can achieve similar modularity without precompiling 
# by using variable assignment:

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

regex = r'\d+'

# Output : None
print(re.search(regex, s1))

# Output: <re.Match object; span=(3, 6), match='123'>
print(re.search(regex,s2))

# Output : <re.Match object; span=(3, 5), match='99'>
print(re.search(regex,s3))

# Output : None
print(re.search(regex,s4))

#--------------------------------------------------------------------------------------------
# In theory, you might expect precompilation to result in faster execution time as well. 
# Suppose you call re.search() many thousands of times on the same regex. It might seem 
# ike compiling the regex once ahead of time would be more efficient than recompiling 
# it each of the thousands of times it’s used.

# In practice, though, that isn’t the case. The truth is that the re module compiles and 
# caches a regex when it’s used in a function call. If the same regex is used subsequently 
# in the same Python code, then it isn’t recompiled. The compiled value is fetched from 
# cache instead. So the performance advantage is minimal.

# All in all, there isn’t any immensely compelling reason to compile a regex in Python. 
# Like much of Python, it’s just one more tool in your toolkit that you can use if you 
# feel it will improve the readability or structure of your code.

#--------------------------------------------------------------------------------------------