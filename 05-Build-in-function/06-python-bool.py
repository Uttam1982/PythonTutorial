# Python bool()
# The bool() method converts a value to Boolean(True or False) using standard truth
# testing procedure
# It's not mandatory to pass a value to bool(). 
# If you don't pass a value, bool() returns False.
# The following values are consider false in python:
# 1. None
# 2. False
# 3. Zero of any numeric type. Example, 0, 0.0, 0j
# 4. Empty sequence. For example '', [], ()
# 5. Empty mapping. For example, {}
# 6. objects of classes which implement __bool()__ or __len()__ which return 0 or False
# All other values except these values are considered true.

# *****************************************************************************************

# Example: How bool() works?

print("No parameter pass to bool() method: ",bool())

test = None
print(test, ' is ', bool(test))

test = False
print(test, ' is ', bool(test))

test = []
print(test, ' is ', bool(test))

test = ()
print(test, ' is ', bool(test))

test = ''
print("''", ' is ', bool(test))

test = 0
print(test, ' is ', bool(test))

test = 0.0
print(test, ' is ', bool(test))

test = 0j
print(test, ' is ', bool(test))

test = 'python'
print(test, ' is ', bool(test))

