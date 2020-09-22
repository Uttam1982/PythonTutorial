#--------------------------------------------------------------------------------------------
# re.sub(<regex>, <repl>, <string>, count=0, flags=0)
#--------------------------------------------------------------------------------------------

# Returns a new string that results from performing replacements on a search string.

# re.sub(<regex>, <repl>, <string>) finds the leftmost non-overlapping occurrences of 
# <regex> in <string>, replaces each match as indicated by <repl>, and returns the result. 
# <string> remains unchanged.

# <repl> can be either a string or a function, as explained below.

#--------------------------------------------------------------------------------------------
# Substitution by String
#--------------------------------------------------------------------------------------------
# If <repl> is a string, then re.sub() inserts it into <string> in place of any 
# sequences that match <regex>:

import re

s = 'foo.123.bar.789.baz'

# Output : foo.#.bar.#.baz
print(re.sub(r'\d+','#',s))

# Output : *.123.*.789.*
print(re.sub(r'[a-z]+','*',s))

#--------------------------------------------------------------------------------------------
# re.sub() replaces numbered backreferences (\<n>) in <repl> with the text of the 
# corresponding captured group:
#--------------------------------------------------------------------------------------------

print(re.sub(r'(\w+),bar,baz,(\w+)',
            r'\2,bar,baz,\1',
            'foo,bar,baz,qux'))

# Here, captured groups 1 and 2 contain 'foo' and 'qux'. In the replacement string 
# '\2,bar,baz,\1', 'foo' replaces \1 and 'qux' replaces \2.

#--------------------------------------------------------------------------------------------

# You can also refer to named backreferences created with (?P<name><regex>) in the 
# replacement string using the metacharacter sequence \g<name>:

# Output : foo,baz,bar,qux
print(re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
            r'foo,\g<w2>,\g<w1>,qux',
            'foo,bar,baz,qux'))

# In fact, you can also refer to numbered backreferences this way by specifying the 
# group number inside the angled brackets:

# Output : foo,baz,bar,qux
print(re.sub(r'foo,(\w+),(\w+),qux',
            r'foo,\g<2>,\g<1>,qux',
            'foo,bar,baz,qux'))


# You may need to use this technique to avoid ambiguity in cases where a 
# numbered backreference is immediately followed by a literal digit character. 

# For example, suppose you have a string like 'foo 123 bar' and want to add a '0' 
# at the end of the digit sequence. You might try this:

# re.error: invalid group reference 10 at position 1
# print(re.sub(r'(\d+)', r'\10', 'foo 123 bar'))


# the regex parser in Python interprets \10 as a backreference to the tenth captured group, 
# which doesn’t exist in this case. Instead, you can use \g<1> to refer to the group:

# Output : foo 1230 bar
print(re.sub(r'(\d+)', r'\g<1>0', 'foo 123 bar'))

# The backreference \g<0> refers to the text of the entire match. 
# This is valid even when there are no grouping parentheses in <regex>:

print(re.sub(r'\d+', r'\g<0>/', 'foo 123 bar'))


# If <regex> specifies a zero-length match, then re.sub() will substitute <repl> 
# into every character position in the string:
print(re.sub('x*', '-', 'foo'))


# In the example above, the regex x* matches any zero-length sequence, so re.sub() 
# inserts the replacement string at every character position in the string—before 
# the first character, between each pair of characters, and after the last character.

#-----------------------------------------------------------------------------------------
# Substitution by Function
#-----------------------------------------------------------------------------------------

import re

def f(match_obj):
  s = match_obj.group(0)  # The matching group

  # s.isdigit() returns True if all characters in s are digit
  if s.isdigit():
    return str(int(s) * 10)
  else:
    return s.upper()


print(re.sub(r'\w+',f,'foo.10.bar.20.baz.30'))

#----------------------------------------------------------------------------------------- 
# Limiting the Number of Replacements
#-----------------------------------------------------------------------------------------

# If you specify a positive integer for the optional count parameter, then re.sub() 
# performs at most that many replacements:

# Output : xxx.xxx.xxx.xxx
print(re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux'))

# Output : xxx.xxx.baz.qux
print(re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux',count=2))


#-----------------------------------------------------------------------------------------
# As with most re module functions, re.sub() accepts an optional <flags> argument as well.