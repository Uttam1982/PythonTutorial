# Example : Dynamic formatting using format()

# dynamic string format template

string = "{:{fill}{align}{width}}"
print(string.format("sara", fill="*",align="^",width=8))

# dynamic float format template
num = "{:{align}{width}.{precision}}"
print(num.format(12.236, align="^",width=9, precision=4))

