# We can use remove() method to remove the given item
# # The remove() method removes the first matching element 

my_list = [12,45,34,45,56,67,45,89,90]
print(my_list)

#in remove we pass the element value not the index 
my_list.remove(45)
print(my_list)


my_list.remove(45)
print(my_list)

# if the element doesn't exist : ValueError
my_list.remove(65)
print(my_list)

