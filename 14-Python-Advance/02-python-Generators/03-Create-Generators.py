# yield statement pauses the function saving all its states and later continues 
# from there on successive calls.
#-------------------------------------------------------------------------------------
# A simple generator function
def my_gen():
  for i in range(3):
    print(f"Before yield: {i}")
    yield i
    print(f"After yield: {i}")


gen = my_gen()

print(next(gen))

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
print(next(gen))

print(next(gen))

# Finally, when the function terminates, StopIteration is raised automatically on further calls
# print(next(gen))
#-------------------------------------------------------------------------------------
# Using for loop
print("-------------------------")
print("Using For Loop\n")
for i in my_gen():
  print(i)


#-------------------------------------------------------------------------------------
iter_obj = my_gen()
print("-------------------------")
print("Using while Loop\n")
while True:
  try:
    element = next(iter_obj)
    print(element)
  except StopIteration:
    break

#-------------------------------------------------------------------------------------  