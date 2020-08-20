# The range() function
# **********************************************************************************
# 1. We can generate a sequence of numbers using range() function. 
# 2. range(10) will generate numbers from 0 to 9 (10 numbers).
# 3. We can also define the start, stop and step size as range(start, stop,step_size). 
# 4. step_size defaults to 1 if not provided.
# 5. This function does not store all the values in memory; it would be inefficient. 
#    So it remembers the start, stop, step size and generates the next number on the go.
# 6. To force this function to output all the items, we can use the function list().

#************************************************************************************
#Example : range() function

# This function does not store all the values in memory
# So it remembers the start, stop, step size and generates the next number on the go.
print(range(10))

# To force this function to output all the items, we can use the function list()
print(list(range(10)))

# step_size defaults to 1 if not provided.
print(list(range(2, 8)))

# step_size 2
print(list(range(2,10,2))) 

# **********************************************************************************

# We can use the range() function in for loops to iterate through a sequence of numbers. 
# It can be combined with the len() function to iterate through a sequence using indexing.

students = ['sam','joe','sara']

for i in range(len(students)):
  print("student name= ",students[i])

#***********************************************************************************




