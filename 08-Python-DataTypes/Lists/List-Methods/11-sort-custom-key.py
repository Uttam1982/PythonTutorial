# Sort with custom function using key
# If you want your own implementation for sorting, the sort() method also accepts a 
# key function as an optional parameter.

# Based on the results of the key function, you can sort the given list.
# list.sort(key=len)

# Alternatively for sorted:
# sorted(list, key=len)

#Example 1: Sort the list using key

# take second element for sort
def takeSecond(elem):
  return elem[1]

#create a list
my_list = [(3,4),(2,3),(4,1),(3,2),(1,3)]
my_list.sort(key=takeSecond)

# print list
print('Sorted list:', my_list)
