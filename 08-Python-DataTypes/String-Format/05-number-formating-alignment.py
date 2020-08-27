# Number formatting with alignment

# The operators <, ^, > and = are used for alignment 
# when assigned a certain width to the numbers.


# <	    Left aligned to the remaining space
# ^	    Center aligned to the remaining space
# >	    Right aligned to the remaining space
# =	    Forces the signed (+) (-) to the leftmost position


# Example : Number formatting with left, right and center alignment

# integer numbers with right alignment
print("The number is: {:5d}".format(12))
print("The number is: {:>5d}".format(12))

# integer left alignment filled with zeros
print("The number is: {:<05d}".format(12))


# float numbers with center alignment
print("The number is: {:^8.3f}".format(12.23456))
print("The number is: {:^08.3f}".format(12.23456))


