# Example : Truncating strings with format()

# truncating strings to 4 letters
print("{:.4}".format('singing'))

# truncating strings to 4 letters
# and padding
print("{:8.4}".format('singing'))

# truncating strings to 4 letters
# and padding and center alignment
print("{:^8.4}".format('singing'))

# truncating strings to 4 letters
# and padding with '*' and center alignment
print("{:*^8.4}".format('singing'))