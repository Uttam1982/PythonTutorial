# What is pass statement in Python?

# 1. In Python programming, the pass statement is a null statement  
# 
# 2. The difference between a comment and a pass statement in Python is that
#    -  while the interpreter ignores a comment entirely, 
#    - pass is not ignored.


# Suppose we have a loop or a function that is not implemented yet, but we want to 
# implement it in the future. They cannot have an empty body. The interpreter would 
# give an error. So, we use the pass statement to construct a body that does nothing.

# Example: pass Statement

'''pass is just a placeholder for
functionality to be added later.'''
sequence = {1,2,3,4,5}
for val in sequence:
  pass

print("pass")

# empty function
def myfunction(args):
  pass

# empty class
class Employee:
  pass