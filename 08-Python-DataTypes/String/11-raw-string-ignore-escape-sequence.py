# Raw String to ignore escape sequence

# Sometimes we may wish to ignore the escape sequences inside a string. 
# To do this we can place r or R in front of the string. 
# This will imply that it is a raw string and any escape sequence inside it will be ignored.

print("This is \x61 \ngood example")

#output
# This is a 
# good example

print(r"This is \x61 \ngood example")
# This is \x61 \ngood example