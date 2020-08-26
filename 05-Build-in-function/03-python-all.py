# Python all()
# The all() method returns True when all elements in the given iterable are true. 
# If not, it returns False.

#*************************************************************************************

# iterable - any iterable (list, tuple, dictionary, etc.) which contains the elements

#                   Truth table for all()
#-----------------------------------------------------------
# When	                                    Return Value
#-----------------------------------------------------------
# All values are true	                        True
# All values are false	                      False
# One value is true (others are false)	      False
# One value is false (others are true)	      False
# Empty Iterable	                            True

#*************************************************************************************

# Example 1: How all() works for lists?

print("using any() for list")
# all values true
l = [1,2,3,4]

print(all(l))

# all values false
l = [0,0,0,0]
print(all(l))

l = [0,False]
print(all(l))

# one false value
l = [1,2,3,4,0]
print(all(l))

l = [1,2,3,4,False]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))
#*************************************************************************************
# Example 2: How all() works for strings?

print("using any() for string")
# True
s = "This is good"
print(all(s))


# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))

#*************************************************************************************
# Example 3: How all() works with Python dictionaries?
print("using any() for dictionary")
d = {0:'False',1:'True'}
print(all(d))

d = {0:'False',False:'True'}  #duplicate key 
print(all(d)) #False
print(d[0]) #True

d={1:'True',2:'True'}
print(all(d))

# Empty iterable true
d = {}
print(all(d))

# 0 is False
# '0' is True
d= {'0':'False'}
print(all(d))



#*************************************************************************************