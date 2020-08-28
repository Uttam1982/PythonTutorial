# Python List insert()
# 1. The list insert() method inserts an element to the list at the specified index.
# 2.   list.insert(i, elem)
# 3. Here, elem is inserted to the list at the ith index. 
# 4. All the elements after elem are shifted to the right.
# 5. The insert() method doesn't return anything; returns None. 
# 6. It only updates the current list.

#***************************************************************************************
# Example : Inserting an Element to the List
list1 = [2,3,4,5]
list1.insert(1,9)
print(list1)

# Example : Inserting a Tuple (as an Element) to the List
mixed_list = [[1,2],{5,6}]
my_tuple = (3,4)
mixed_list.insert(1,my_tuple)
print(mixed_list)

#***************************************************************************************
