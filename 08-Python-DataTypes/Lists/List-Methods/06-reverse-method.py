#**************************************************************************************************
# Python List reverse()
#**************************************************************************************************

# 1. The reverse() method reverses the elements of the list.

# 2. list.reverse()

# 3. The reverse() method doesn't take any arguments.

# 4. The reverse() method doesn't return any value. It updates the existing list.

#**************************************************************************************************

#initialize a list
my_list = ['Sara','Ben','Joe','Alice']
print("original: ",my_list)

# Example: Reverse a List
my_list.reverse()
print("Reversed: ",my_list)

#**************************************************************************************************
# Example : Reverse a List Using Slicing Operator

my_list = ['Sara','Ben','Joe','Alice']
print("original: ",my_list)

reverse_list = my_list[::-1]
print("Reversed: ",reverse_list)

#**************************************************************************************************
# Example : Accessing Elements in Reversed Order

my_list = ['Sara','Ben','Joe','Alice']

for name in reversed(my_list):
  print(name)

#**************************************************************************************************

