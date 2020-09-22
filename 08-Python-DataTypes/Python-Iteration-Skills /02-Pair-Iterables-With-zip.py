# 2. Pair Iterables With zip()
#-------------------------------------------------------------------------------------------
# When we have a few iterables to begin with and need to retrieve items 
# from each of these iterables at the same positions, 
# we should consider the zip() function, as shown in this example.

#-------------------------------------------------------------------------------------------
# Two iterables
students = ['Sam','Joe','Sara','Ben']
scores = [98,78,89,90]

# the basic way
print()
for i in range(len(students)):
  student = students[i]
  score = scores[i]
  print(f"Student {student}: {score}")

# using zip() function:
print("# using zip() function:")
for student ,score in zip(students,scores):
  print(f"Student {student}: {score}")

#-------------------------------------------------------------------------------------------
# The zip() function can join multiple iterables and in each loop, 
# it produces a tuple object that comprise elements from each iterable 
# at the same index. We can unpack the tuple object to retrieve the 
# elements very conveniently.


# Another thing to note is that the zip() function will zip the iterables 
# matching the shortest iterable among them. 
# 
# If you want the zipping matching the longest iterable, you should use 
# zip_longest() function in the itertools library.

#-------------------------------------------------------------------------------------------