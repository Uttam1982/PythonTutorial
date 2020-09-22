# A simple generator function
def my_gen():
  n = 1
  print('This is printed first')

  # The generator function contains yeids statements
  yield n

  n += 1
  print('This is printed second')
  yield n

  n += 1
  print('This is printed third')
  yield n


# It returns an object but does not start execution immediately.
gen = my_gen()

# We can iterate through the items using next().
print(next(gen))

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(gen))

# We can iterate through the items using next().
print(next(gen))

# Finally, when the function terminates, StopIteration is raised automatically on further calls
# print(next(gen))

# ** One interesting thing to note in the above example is that 
# The value of variable n is remembered between each call.

# One final thing to note is that we can use generators with for loops directly.
print("-------------------------------")
#using for loop
for i in my_gen():
  print(i)