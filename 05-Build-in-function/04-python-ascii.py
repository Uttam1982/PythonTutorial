#Python ascii()
# The ascii() method return a string containing a printable representation of an object
# It escape the non ascii characters in the string using \x, \u or \U escapes

# ascii() method takes an object like (string, list etc)

# **************************************************************************************
# working with string
# Example 1: How ascii() method works?

text1 = 'Python is interesting'
print(ascii(text1))

text2 = 'Pythön is interesting'
print(ascii(text2))

#For example, ö is changed to \xf6n, √ is changed to \u221a

print('Pyth\xf6n is interesting')

# **************************************************************************************
# working with list
l =['python','Pythön',5]
print(ascii(l))