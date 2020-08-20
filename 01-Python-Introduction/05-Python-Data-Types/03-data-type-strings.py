# Python Strings

# - String is sequence of Unicode characters
# - We can use single quotes or double quotes to represent strings.
# - Multi-line strings can be denoted using triple quotes, ''' or """

strings_double_quotes = "This is a double quotes string"
strings_single_quotes = 'This is a single quote string'
multiline ="""This
is a multiline
string"""


print(strings_double_quotes)
print(strings_single_quotes)
print(multiline)

#a Unicode literal 
unicode = u"\u00dcnic\u00f6de"
print(unicode)
print(type(unicode))

# We can use the slicing operator [] to extract items but we cannot change its value.
# Strings are immutable.

S = 'PYTHON PROGRAMMING' 

#S[4] = 'O'
print("S[4] = ",S[4])

# S[6:11] = 'PROG'
print("S[7:12] = ",S[6:11])

# Generates error
# Strings are immutable in Python
S[5] ='d'

