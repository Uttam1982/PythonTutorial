#-------------------------------------------------------------------------------------------
# 1. Track Iteration With enumerate()
#-------------------------------------------------------------------------------------------

# 1. Suppose that we need to track the counting of the iteration. 
# 2. In other words, we want to know how many loops we have iterated. 
# 3. In this case, we should consider the enumerate() function.

#-------------------------------------------------------------------------------------------

# A iterable to start with
numbers = ['one','two','three','four']

# The basic way 
print("using for loop")
for i in range(len(numbers)):
  print(f"# {i+1} : {numbers[i]}")

#-------------------------------------------------------------------------------------------

# Use enumerate()
print("# Use enumerate()")
for i, number in enumerate(numbers,1):
  print(f"# {i}: {number}")

#-------------------------------------------------------------------------------------------

# The enumerate() function creates an enumerate object as an iterator. 
# It can take an optional argument start, which specifies the start of the counter. 
# By default, it starts the counting from 0. 
# In our case, we starts to count the first rendered element from 1. 
# As you can see, the enumerate() function directly gives us the counter and the element.

#-------------------------------------------------------------------------------------------