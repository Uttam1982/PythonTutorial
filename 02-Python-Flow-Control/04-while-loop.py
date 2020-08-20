# What is while loop in Python?
#************************************************************************************

# The while loop in Python is used to iterate over a block of code as long as 
# the test expression (condition) is true.

#************************************************************************************
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user
n = int(input("Enter n: "))
#n = 10

# initialize sum and counter
sum =0
i = 0

while i <= n:
  sum = sum +i
  i = i+1    #update the counter

# print the sum
print('The sum is ',sum)


#************************************************************************************
# While loop with else
#************************************************************************************

# Same as with for loops, while loops can also have an optional else block.

# The else part is executed if the condition in the while loop evaluates to False.

# The while loop can be terminated with a break statement. In such cases, the else 
# part is ignored. 
# Hence, a while loop's else part runs if no break occurs and the condition is false.

'''Example to illustrate
the use of else statement
with the while loop'''

i =0 


while i < 3:
  print('hello world!')
  # if i == 2:
  #   break
  i = i + 1
else:
  print("inside else block !")