#-------------------------------------------------------------------
# for element in iterable:
#     # do something with element
#-------------------------------------------------------------------
#define a list
numbers = ["one","two","three"]

for element in numbers:
  print(element)


#-------------------------------------------------------------------
# Is actually implemented as.
#-------------------------------------------------------------------
iter_obj = iter(numbers)

while True:
  try:
    # get the next item
    element = next(iter_obj)
    # do something with element
    print(element)
  except StopIteration:
    # if StopIteration occurs, break from the loop 
    break

#-------------------------------------------------------------------

# So internally, the for loop creates an iterator object, 
# iter_obj by calling iter() on the iterable.

# Ironically, this for loop is actually an infinite while loop.

#-------------------------------------------------------------------