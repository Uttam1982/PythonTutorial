# Conversion between data types
# We can convert between different data types by using different 
# type conversion functions like int(), float(), str(), etc.


# Example converting int to float
print(float(5)) # 5.0

# Example converting float  to int will truncate the value (make it closer to zero).
print(int(3.7))  # 3
print(int(- 3.7))  # -3

# Example convertion to and from string
# string must contain compatible values.

print(float('3.7'))
print(int('5'))

print(str(25))
print(str('- 3.7'))

print(int('5p')) #ValueError: invalid literal for int() with base 10: '5p'

