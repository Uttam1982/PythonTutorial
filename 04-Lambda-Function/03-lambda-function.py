#------------------------------------------------------------------
# Lambda Expression with One Parameter
#------------------------------------------------------------------
def square(num):
  return num**2

print("square of 5: ",square(5))

square = lambda num : num**2
print("square of 5 using lambda: ",square(5))

#------------------------------------------------------------------
#Lambda Expression with Multiple Parameters
#------------------------------------------------------------------
def sum(num1, num2):
  return num1 + num2 

print("Sum of 3 and 4 is: ",sum(3,4))

# using lambda keyword that returns the sum of num1 and num2
sum = lambda num1, num2 : num1 + num2
print("Sum of 3 and 4 using lambda is: ",sum(3,4))

#------------------------------------------------------------------
# Conditional Statements in Lambda Expressions
#------------------------------------------------------------------
# function that takes in num1 and num2 and returns the larger number

def large_num(num1,num2):
  if num1 > num2:
    return num1
  else:
    return num2

print("The large number is:",large_num(8,4))

#using lambda epression
large_num = lambda num1, num2 : num1 if num1 > num2 else num2
print("The large number using lambda function is:",large_num(8,4))

#------------------------------------------------------------------
# What About else if?
#------------------------------------------------------------------
large_num = lambda num1, num2 : num1 if num1 > num2 else (num2 if num1 < num2 else 'They are equal')
print("The large number using lambda function is:",large_num(8,8))


#------------------------------------------------------------------

