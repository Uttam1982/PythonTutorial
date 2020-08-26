# Example of Lambda Function in python

# Program to show the use of lambda functions

# d= def double(x):
#     return x * 2

# d = lambda (x) : return x * 2 

double = lambda x : x * 2
print("double= ",double(5))

#*****************************************************************************
## a and b are the arguments and a*b is the expression which gets 
# evaluated and returned.    

mul = lambda a, b: a * b
print("mul= ",mul(2, 5))

#*****************************************************************************
# The function table(n) prints the table of n    

def table(n):
  return lambda x: x * n

n = int(input("Enter the number: "))

b = table(n)

for i in range(1, 11):
  print(n," X ",i," = ",b(i))






