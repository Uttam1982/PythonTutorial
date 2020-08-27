# Example : Number formatting for signed numbers

#simple formating
print("{:f} {:f}".format(12.34, -12.34))

# show the + sign
print("{:+f} {:+f}".format(12.34, -12.34))

# show only - sign
print("{:-f} {:-f}".format(12.34, -12.34))

# show space for + sign
print("{: f} {: f}".format(12.34, -12.34))