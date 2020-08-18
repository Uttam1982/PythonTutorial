# Python Comments
# - In Python, we use the hash (#) symbol to start writing a comment.
# - Python Interpreter ignores comments.

#This is a comment
# print out uttam

print('uttam')


# Multi-line comments
# - One way is to use the hash(#) symbol at the beginning of each line.

#This is a long comment
#and it extends
#to multiple lines


# - Another way of doing this is to use triple quotes, either ''' or """.

"""This is a long comment
and it extends
to multiple lines"""


#Docstrings in Python

# - A docstring is short for documentation string.
# - Python docstrings (documentation strings) are the string literals that 
#   appear right after the definition of a function, method, class, or module.

def double(num):
  """Function to double the value"""
  return 2 * num

# - The docstrings are associated with the object as their __doc__ attribute.

# - So, we can access the docstrings of the above function with the following lines of code:

print(double.__doc__)