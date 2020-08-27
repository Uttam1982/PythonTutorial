# Simple number formatting

# integer arguments
print("The number is: {:d}".format(345))

# float arguments : Displays fixed point number (Default: 6)
print("The number is: {:f}".format(345.123456789))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))