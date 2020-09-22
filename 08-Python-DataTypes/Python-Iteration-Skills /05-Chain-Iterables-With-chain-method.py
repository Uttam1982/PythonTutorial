# 5. Chain Iterables With chain()

# In a previous section, we’ve talked about how to work with multiple iterables using the zip() 
# function, for which, you can think of that we concatenate iterables in the vertical direction. 

# If you want to concatenate iterables head to tail, you should use the chain() function in the 
# itertools library. Specifically, suppose that you have multiple iterables, you want to iterate 
# each of them sequentially, which is a best use case of the chain() function.

from itertools import chain

# Iterables 
list1 = ["one","two","three"]
list2 = ["four","five","six"]
tuple1 =("seven","eight","nine")

numbers = list1 + list2

# TypeError: can only concatenate list (not "tuple") to list
# numbers2 = list1 + tuple1

# The typical way
print("# The typical way")
for num in numbers:
  print(num)

# use chanin method:
print("# use chain method for list")
for num in chain(list1,list2):
  print(num)

print("# use chanin method for list and tuple")
for num in chain(list1,tuple1):
  print(num)


  # The typical way involves concatenating the iterables manually, such as 
  # using an intermediate list. If you work with other iterables, such as 
  # dictionaries and sets, you need to know how to concatenate them.

  # The chain() function can chain any number of iterables and make another 
  # iterator that produces elements sequentially from each of the iterables. 
  # You don’t need to manage another temporary object that holds these elements.
