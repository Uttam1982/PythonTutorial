# Example : Number formatting with padding for int and floats

# integer numbers with minimum width
print("The number is:{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("The number is:{:2d}".format(12345))

# padding for float numbers
# floats has both integer and decimal parts. And, 
# the mininum width defined to the number is for 
# both parts as a whole including ".".

print("The number is:{:8.3f}".format(234.23456789))

# integer numbers with minimum width filled with zeros
print("The number is:{:05d}".format(12))

# padding for float numbers filled with zeros
print("The number is:{:08.3f}".format(234.23456789))

