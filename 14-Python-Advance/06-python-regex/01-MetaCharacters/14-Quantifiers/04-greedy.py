#--------------------------------------------------------------------------------------------
# *?
# +?
# ??
#--------------------------------------------------------------------------------------------

# The non-greedy (or lazy) versions of the *, +, and ? quantifiers.

# When used alone, the quantifier metacharacters *, +, and ? are all greedy, 
# meaning they produce the longest possible match

# Consider this example:
#--------------------------------------------------------------------------------------------
import re

# Output : <re.Match object; span=(2, 16), match='<foo> <> <bar>'>
print(re.search('<.*>',' %<foo> <bar> <baz>%'))

# The regex <.*> effectively means:

# A '<' character
# Then any sequence of characters
# Then a '>' character
# But which '>' character? There are three possibilities:

# The one just after 'foo'
# The one just after 'bar'
# The one just after 'baz'
# Since the * metacharacter is greedy, it dictates the longest possible match, 
# which includes everything up to and including the '>' character that follows 'baz'. 
# You can see from the match object that this is the match produced.

#--------------------------------------------------------------------------------------------
# non-greedy metacharacter sequence *?
#--------------------------------------------------------------------------------------------

# If you want the shortest possible match instead, 
# then use the non-greedy metacharacter sequence *?:


# Output : <re.Match object; span=(2, 16), match='<foo> <> <bar>'>
print(re.search('<.*?>',' %<foo> <bar> <bar>%'))


# In this case, the match ends with the '>' character following 'foo'.

#--------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(2, 16), match='<foo> <bar> <baz>'>
print(re.search('<.+>','%<foo> <bar> <bar>%'))


# Output : <re.Match object; span=(2, 16), match='<foo> <> <bar>'>
print(re.search('<.+?>','%<foo> <bar> <bar>%'))


# similar to the examples shown above, only using + and +? instead of * and *?.

#--------------------------------------------------------------------------------------------

# Output : <re.Match object; span=(8, 10), match='<>'>
print(re.search('<.?>',' %<foo> <> <baz>%'))

# Output : <re.Match object; span=(8, 11), match='<b>'>
print(re.search('<.?>',' %<foo> <b> <baz>%'))

# Output : None
print(re.search('<.?>',' %<foo> <bar> <baz>%'))


#--------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 2), match='ba'>
print(re.search('ba?', 'baaaa'))

# Output : <re.Match object; span=(0, 1), match='b'>
print(re.search('ba??', 'baaaa'))

# In general, the ? metacharacter matches zero or one occurrences of the preceding regex. 
# The greedy version, ?, matches one occurrence, so ba? matches 'b' followed by a single 'a'. 

# The non-greedy version, ??, matches zero occurrences, so ba?? matches just 'b'.

#--------------------------------------------------------------------------------------------