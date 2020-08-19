# Numeric literals
# - Numeric literals are immutable(unchangable)
# - 3 different numerical types: Integer, Float, and Complex


#Example 4: How to use Numeric literals in Python?

num1 = 0b1010   # Binary Literals
num2 = 100      # Decimal Literals
num3 = 0o310    #Octal literals
num4 = 0x12c    #Hexadecimal Liyerals

print(num1)
print(type(num1))

print(num2)
print(type(num2))

print(num3)
print(type(num3))

print(num4)
print(type(num4))

#Float Literals
f1 = 10.5
f2 = 1.5e2   #equivalent to 1.5 * 10^2.

print(f1)
print(type(f1))

print(f2)
print(type(f2))

#Complex Literals
# Complex numbers are written in the form, x + yj, 
# where x is the real part and y is the imaginary part.

x = 1 + 3.14j
print(x, x.imag, x.real)
print(type(x))







