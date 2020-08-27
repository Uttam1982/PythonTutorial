# reverse() method
# The reverse() method reverses the elements of the list

# Example 1: Reverse a List
my_list= ['sam','joe','rita']
print('original list: ',my_list)
print("The reverse() method doesn't return any value: ", my_list.reverse()) 
print('updated list: ',my_list)


# Example 2: Reverse a List Using Slicing Operator
my_list= ['sam','joe','rita']
print('original list: ',my_list)

#Syntax: reversed_list = systems[start:stop:step] 
reversed_list = my_list[::-1]
print('updated list: ',reversed_list)


# Example 3: Accessing Elements in Reversed Order
my_list= ['sam','joe','rita']

# Printing Elements in Reversed Order
for i in reversed(my_list):
  print(i)