# String Literal
# - A string literal is a sequence of characters surrounded by quotes.
# - We can use both single, double, or triple quotes for a string.
# - a character literal is a single character surrounded by single or double quotes.

#Example : How to use string literals in Python?

#string literal
strings = "This is python"
print(strings)
print(type(strings))

#a character literal.
char= "C"  
print(char)
print(type(char))

#multi-line string literal
multiline_str = """This 
is 
multiline 
string"""

print(multiline_str)
print(type(multiline_str))

#a Unicode literal 
unicode = u"\u00dcnic\u00f6de"
print(unicode)
print(type(unicode))

#raw string literal.
raw_str = r"raw \n string" 
print(raw_str)
print(type(raw_str))