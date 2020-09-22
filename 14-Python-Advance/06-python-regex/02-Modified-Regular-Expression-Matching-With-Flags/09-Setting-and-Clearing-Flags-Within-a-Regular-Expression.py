# Setting and Clearing Flags Within a Regular Expression
#----------------------------------------------------------------------------------------------
# you can also modify flag values within a regex in Python. 
# There are two regex metacharacter sequences that provide this capability.

#----------------------------------------------------------------------------------------------
# (?<flags>)
#----------------------------------------------------------------------------------------------
# Sets flag value(s) for the duration of a regex.

# Within a regex, the metacharacter sequence (?<flags>) sets the specified 
# flags for the entire expression.

# The value of <flags> is one or more letters from the set a, i, L, m, s, u, and x. 
# Here’s how they correspond to the re module flags:
#----------------------------------------------------------------------------------------------
# Letter	Flags
# a	re.A     re.ASCII
# i	re.I     re.IGNORECASE
# L	re.L     re.LOCALE
# m	re.M     re.MULTILINE
# s	re.S     re.DOTALL
# u	re.U     re.UNICODE
# x	re.X     re.VERBOSE

#----------------------------------------------------------------------------------------------
import re

# Combining <flags> Arguments in a Function Call

# Output : <re.Match object; span=(4, 7), match='BAR'>
print(re.search('^bar', 'FOO\nBAR\nBAZ\n', re.I|re.M))

#----------------------------------------------------------------------------------------------
# Setting Flags Within a Regular Expression
# (?<flags>)
#----------------------------------------------------------------------------------------------

# The following examples are equivalent way of setting the IGNORECASE and MULTILINE flags:

# Output : <re.Match object; span=(4, 7), match='BAR'>
print(re.search('(?im)^bar', 'FOO\nBAR\nBAZ\n', re.I|re.M))

#----------------------------------------------------------------------------------------------

# Note that a (?<flags>) metacharacter sequence sets the given flag(s) 
# for the entire regex no matter where you place it in the expression:

import re

# Output : <re.Match object; span=(0, 11), match='foo\nbar\nbaz'>
print(re.search('foo.bar(?s).baz', 'foo\nbar\nbaz'))

# Output : <re.Match object; span=(0, 11), match='foo\nbar\nbaz'>
print(re.search('foo.bar.baz(?s)', 'foo\nbar\nbaz'))

# As of Python 3.7, it’s deprecated to specify (?<flags>) anywhere 
# in a regex other than at the beginning:

# It still produces the appropriate match, but you’ll get a warning message.

import sys
# Output : 3.7.3 (default, Apr 24 2020, 18:51:23) 
print(sys.version)


#----------------------------------------------------------------------------------------------
# (?<set_flags>-<remove_flags>:<regex>)
#----------------------------------------------------------------------------------------------
# Sets or removes flag value(s) for the duration of a group.

# (?<set_flags>-<remove_flags>:<regex>) defines a non-capturing group that matches 
# against <regex>. For the <regex> contained in the group, the regex parser sets 
# any flags specified in <set_flags> and clears any flags specified in <remove_flags>.

# Values for <set_flags> and <remove_flags> are most commonly i, m, s or x.

#  (?<set_flags>:<regex>)

# Output : <re.Match object; span=(0, 6), match='FOObar'>
print(re.search('(?i:foo)bar', 'FOObar'))

# Output : None
print(re.search('(?i:foo)bar', 'FOOBAR'))

# As in the previous example, the match against 'FOO' would succeed because 
# it’s case insensitive. But once outside the group, IGNORECASE is no longer 
# in effect, so the match against 'BAR' is case sensitive and fails.


#  (?-<remove_flags>:<regex>)
# Output : None
print(re.search('(?-i:foo)bar', 'FOOBAR', re.IGNORECASE))

# Again, there’s no match. Although re.IGNORECASE enables case-insensitive 
# matching for the entire call, the metacharacter sequence (?-i:foo) 
# turns off IGNORECASE for the duration of that group, so the match 
# against 'FOO' fails.

# As of Python 3.7, you can specify u, a, or L as <set_flags> 
# to override the default encoding for the specified group:

s = 'sch\u00f6n'

# Output : <re.Match object; span=(0, 3), match='sch'>
print(re.search(r'(?a:\w+)',s))

# Output : <re.Match object; span=(0, 5), match='schön'>
print(re.search(r'(?u:\w+)',s))

# You can only set encoding this way, though. You can’t remove it:

# Output : re.error: bad inline flags: cannot turn off flags 'a', 'u' and 'L' at position 4
print(re.search(r'(?-a:\w+)',s))

# u, a, and L are mutually exclusive. Only one of them may appear per group.