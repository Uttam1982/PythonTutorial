#**************************************************************************************************
# Python List sort()
# #**************************************************************************************************

# 1. The sort() method sorts the elements of a given list in a specific ascending 
#    or descending order.

# 2. list.sort(key=..., reverse=...)

# 3. Alternatively, you can also use Python's built-in sorted() function for the same purpose.

# 4. By default, sort() doesn't require any extra parameters. 
#    However, it has two optional parameters:
#    1. reverse - If True, the sorted list is reversed (or sorted in Descending order)
#    2. key - function that serves as a key for the sort comparison

# 5. The sort() method doesn't return any value. Rather, it changes the original list.

# 6. If you want a function to return the sorted list rather than change the original list, 
#    use sorted().

#**************************************************************************************************

# name list
name_list = ['Sara','Joe','Ben','Alex','Dave']
print('original: ',name_list)

# sort in acending order
# sort() changes the original list
name_list.sort()
print('sorted list ascending order: ',name_list)

#**************************************************************************************************
#Sort in Descending order
name_list.sort(reverse=True)
print('sorted list descending order: ',name_list)

#**************************************************************************************************

#Sort with custom function using key
name_list = ['Sara','Joe','Ben','Alex','David']
name_list.sort(key=len)
print('sorted list ascending order: ',name_list)

#Here, len is the Python's in-built function to count the length of an element.
#**************************************************************************************************

# Example : Sort the list using key

# take second element to sort
def takeSecond(elem):
  return elem[1]

my_list = [(4,3),(2,2),(3,1),(2,4)]
print("original: ",my_list)
my_list.sort(key=takeSecond)
print("Sorted list :",my_list)

#**************************************************************************************************
