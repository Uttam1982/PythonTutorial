# What is for loop in Python?
# **********************************************************************************

# - The for loop in Python is used to iterate over a sequence (list, tuple, string) 
#   or other iterable objects. 
# - Iterating over a sequence is called traversal.

# **********************************************************************************

# Example: # Program to find the sum of all numbers stored in a list

numbers = [2,3,4,5,6,7,8,4,9]

sum = 0

for val in numbers:
  sum = sum + val

print("The sum is: ",sum)

# Here, val is the variable that takes the value of the item inside the sequence 
# on each iteration.

# **********************************************************************************
# for loop with else
# **********************************************************************************

# 1. A for loop can have an optional else block as well. 
# 2. The else part is executed if the items in the sequence used in for loop exhausts.
# 3. The break keyword can be used to stop a for loop. In such cases, the else part is ignored.
# 4. Hence, a for loop's else part runs if no break occurs.

digits = [1,5,7]

for d in digits:
  print(d)
else:
  print("No items left")

# **********************************************************************************

digits = [1,5,7]

for d in digits:
  print(d)
  if d > 6:
    break
  
else:
  print("No items left")


# **********************************************************************************
# program to display student's marks from record

marks = {'sam':89, 'joe':95, 'sara':98}

student_name = input("Enter the student name: ")

for name in marks:
  if name == student_name:
    print(name," your marks is ",marks[name])
    break
else:
  print("No entry with the name found")

