# Special operators
# Python language offers some special types of operators like 
# the identity operator or the membership operator.

# ******************************************************************************************
# Identity Operator
# is and is not are the identity operators in Python. 
# ******************************************************************************************
# They are used to check if two values (or variables) are located on the same part of the memory. 
# Two variables that are equal does not imply that they are identical.

int1 = 5
int2 = 5

string1 = 'python'
string2 = 'python'

lst1 = [1,2,3]
lst2 = [1,2,3]

print('int1 is int2: ',int1 is int2 )
print('int1 is not int2: ',int1 is not int2 )
# we see that int1 and int2 are integers of the same values, 
# so they are equal as well as identical.

print('string1 is string2: ',string1 is string2 )
print('string1 is not string2: ',string1 is not string2 )
# Same is the case with x2 and y2 (strings).

print('lst1 is lst2: ',lst1 is lst2 )
print('lst1 is not lst2: ',lst1 is not lst2 )

# But lst1 and lst2 are lists. They are equal but not identical. 
# It is because the interpreter locates them separately in memory although they are equal.
