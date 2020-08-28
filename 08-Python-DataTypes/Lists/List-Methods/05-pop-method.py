# Python List pop()
#**************************************************************************************************
# 1. The pop() method removes the item at the given index from the list and returns the removed item.

# 2. list.pop(index)

# 3. The argument passed to the method is optional. If not passed, the default index -1 

#    is passed as an argument (index of the last item).

# 4. If the index passed to the method is not in range, it throws IndexError: 
#    pop index out of range exception.

# 5. The pop() method returns the item present at the given index. 
#    This item is also removed from the list.
#**************************************************************************************************

#initialize a list
my_list = [10,20,30,40,50,60,70,80,90]
print("original list: ",my_list)

#using pop() method
#remove and return the 3rd element 

#output 30
print("my_list.pop(2): ",my_list.pop(2))
print("updated list: ",my_list)

#pop() without an index, and for negative indices
# default index -1

#output 90
print("my_list.pop():",my_list.pop())
print("updated list: ",my_list)

#negative index

#output 70
print("my_list.pop(-2):",my_list.pop(-2))
print("updated list: ",my_list)


#**************************************************************************************************

