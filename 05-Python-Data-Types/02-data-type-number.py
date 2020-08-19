# Python Numbers
# Integers, floating point numbers and complex numbers
# They are defined as int, float and complex classes in Python
# We can use the type() function to know which class a variable or a value belongs to.
# the isinstance() function is used to check if an object belongs to a particular class.


a = 10
print("Value of a = ",a)
print("Type of a = ",type(a))
print(a, "is integre number?", isinstance(a,int))


b = 5.1
print("Value of b = ",b)
print("Type of b = ",type(b))
print(b, "is floating number?", isinstance(b,float))

# Complex numbers are written in the form, x + yj, 
# where x is the real part and y is the imaginary part. 

c = 1 + 5j
print("Value of c = ",c)
print("Type of c = ",type(c))
print(c, "is complex number?", isinstance(c,complex))


# Integers can be of any length, it is only limited by the memory available.
a = 1234567890123456789
print(a)

# A floating-point number is accurate up to 15 decimal places
b = 0.1234567890123456789
print(b)
# Notice that the float variable b got truncated.
