# Python Recursive Function
# In Python, we know that a function can call other functions. 
# It is even possible for the function to call itself. 
# These types of construct are termed as recursive functions.


def factorial(x):
  '''
  This is a recersive function
  to find the factorial of an integer
  '''
  if x == 1:
    return 1
  else:
    return x * factorial(x-1)


num = 5
print("The factorial of ",num, " is",factorial(5))


#Explanation
# factorial(3)          # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call
