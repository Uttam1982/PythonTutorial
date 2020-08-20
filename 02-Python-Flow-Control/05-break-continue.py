# Python break statement
#*****************************************************************************************
# 1. The break statement terminates the loop containing it. 
# 2. Control of the program flows to the statement immediately after the body of the loop.
# 3. If the break statement is inside a nested loop (loop inside another loop), 
# 4. the break statement will terminate the innermost loop.

for val in 'python':
  if val == 't':
    break
  print(val)

print('The end')


#*****************************************************************************************
# Python continue statement
#*****************************************************************************************

# 1. The continue statement is used to skip the rest of the code inside a loop for the current 
#    iteration only. 
# 2. Loop does not terminate but continues on with the next iteration.


for val in 'python':
  if val == 't':
    continue
  print(val)

print('The end')