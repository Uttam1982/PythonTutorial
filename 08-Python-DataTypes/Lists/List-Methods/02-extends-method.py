# Python List extend()
# 1. The extend() method adds all the elements of list, tuple, string etc. to the end of the list.
# 2. The syntax of the extend() method is:
      #list1.extend(iterable)
# 3. Here, all the elements of iterable are added to the end of list1.
# 4. the extend() method takes an iterable such as list, tuple, string etc.
# 5. The extend() method modifies the original list. It doesn't return any value.

#**************************************************************************************************

#initialize a names list
names = ['Sara','Joe','Ben']
print("original list: ",names)

# create a new_names list
new_names = ['Alex','Dave']

# use extends to add all elements of new_list at the end 
names.extend(new_names)
print("extended list after adding a list: ",names)

#**************************************************************************************************
# Example : Add Elements of Tuple and Set to List

#initialize a names list
names = ['Sara','Joe','Ben']
print("original list: ",names)

# create a tuple
my_tuple = ('Alex','Dave')

# use extends to add all elements of tuple
names.extend(my_tuple)
print("Extended list after adding tuple: ",names)

#**************************************************************************************************
# create a set
my_set = {'Rita','John'}

# use extends to add all elements of set
names.extend(my_set)
print("Extended list after adding set: ",names)


#**************************************************************************************************
# Other Ways to Extend a List

# You can also append all elements of an iterable to the list using:
# 1. the + operator
# 2. the list slicing syntax

# using 1. the + operator
list1 = [1,2,3,4]
list2 = [4,5,6,7]

list1 += list2
#output [1, 2, 3, 4, 4, 5, 6, 7]
print(list1)

#**************************************************************************************************
# using the list slicing syntax

list1 = [1,2,3,4]
list1[4:8]= [5,6,7,8]
print(list1)

print(len(list1))

list1[len(list1):] = [9,10]
print(list1)

#**************************************************************************************************
# Python extend() Vs append()

l1 = [1,2]
l2 = [1,2]

a = (3,4)

l1.append(a)
print(l1)

l2.extend(a)
print(l2)






