#-------------------------------------------------------------------------------------------
# 3. Reverse Iteration With reversed()
#-------------------------------------------------------------------------------------------

# When you need to iterate a sequence of elements in the reverse order, 
# it’s best to use the reversed() function. 

# Suppose that students arrive at the classroom at slightly different times, 
# you want to check their assignments using the reverse order

#-------------------------------------------------------------------------------------------

# The student arrival records
students_arrived = ['Sam','Ben','Joe','Sara']

# The typical ways
print("use range() function")
for i in range(1, len(students_arrived)+1):
  print(f"{students_arrived[-i]}")


#using indexing
print("use indexing [::-1]")
for i in students_arrived[::-1]:
  print(i)
  
# Use reversed()
print("Use reversed() function")
for i in reversed(students_arrived):
  print(i)

#-------------------------------------------------------------------------------------------

# If you stick with the range() function, you’ll use the reverse indexing of the sequence. 
# In other words, we use -1 to refer to the last item of the list and so on.

# Alternatively, we can reverse the list using [::-1] and then iterate the 
# new created list object.

# The best way to do is just simply use the reversed() function. 
# It is a very flexible function, because it can take other sequence data, 
# such as tuples and strings.

#-------------------------------------------------------------------------------------------