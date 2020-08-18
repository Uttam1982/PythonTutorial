# Multi-line statement

# In Python, the end of a statement is marked by a newline character.
# We can make a statement extend over multiple lines with the line continuation character (\). 
# For example: 

a = 1+2+3+\
    4+5+6+\
    7+8+9
print("line continuation character (\): ",a)

# This is an explicit line continuation.

# In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }. 

a = (1+2+3+
    4+5+6+
    7+8+9)
print("line continuation is implied inside parentheses ( ): ",a)

#the surrounding parentheses ( ) do the line continuation implicitly.


#Same is the case with [ ] and { }

names = ['sam',
         'Joe',
         'rita']
print(names)

# We can also put multiple statements in a single line using semicolons, as follows:
a =1; b=2; c=3
print(a,b,c)