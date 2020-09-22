#-------------------------------------------------------------------------------------------
# 4. Filter Elements With filter()
#-------------------------------------------------------------------------------------------

# You don’t always need to use all the items in the iterable. 
# In these cases, we can usually check if items satisfy particular criteria before 
# we apply the needed operations. Such condition evaluation and creation of the 
# needed iterator can be easily integrated into one function call — filter(). 
# Let’s see how it works in comparison to the typical way.

#-------------------------------------------------------------------------------------------

# A list of numbers to process

numbers = [12,23,34,45,56,67,78,89,90]

#typical ways
print('typical ways')
for num in numbers:
  if num%2:
    print("odd number: ",num)

#typical ways
for num in numbers:
  if num%2 ==0:
    print("even number: ",num)

# using filter()
print('using filter() functions')
for num in filter(lambda x: x%2, numbers):
  print("odd number: ",num)


