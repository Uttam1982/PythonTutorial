# Python any()
# The any() function returns True if any element of an iterable is True. 
# If not, any() returns False.

#*************************************************************************************

# Condition	                                Return Value
# -------------------------------------------------------
# All values are true	                      True
# All values are false	                    False
# One value is true (others are false)	    True
# One value is false (others are true)	    True
# Empty Iterable	                          False

#*************************************************************************************

#Example 1: Using any() on Python Lists
# The any() method works in a similar way for tuples and sets like lists.

print('Using any() on Python Lists')
# True since 1,3 and 4 (at least one) is true
l = [1,3,2,7]
print(any(l))

# False since both are False
l1 = [0, False]
print(any(l1))

# True since 5 is true
l2 = [0, False, 5]
print(any(l2))

# False since iterable is empty
l3 = []
print(any(l3))

#*************************************************************************************

#Example 2: Using any() on Python Strings
print('Using any() on Python Strings')

s= 'This is a string'
print(any(s))

s = "0000"
print(any(s))

s = "False"
print(any(s))

s = ''
print(any(s))

#*************************************************************************************

#Example 3: Using any() with Python Dictionaries
print('Using any() with Python Dictionaries')

# 0 is False
d = {0:'abc',False:'xyz'}
print(any(d))

d = {0:'abc','False':'xyz'}
print(any(d))

# 1 is True
d = {0:'False',1:'True'}
print(any(d))

# Iterable empty 
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': False}
print(any(d))

d = {0: 'False'}
print(any(d))
