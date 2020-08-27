# insert() method

# we can insert one item at a desired location by using the method insert() 
# insert multiple items by squeezing it into an empty slice of a list.


# Demonstration of list insert() method
my_list = [1,9]

#If index is 1, the element is inserted before the 2nd element. Its position will be 2nd.
my_list.insert(1,2)
print(my_list)                  #[1, 2, 9]

#If index is -1, the element is inserted before the last element.
my_list.insert(-1,5)      
print(my_list)                  #[1, 2, 5, 9]

my_list.insert(-2,15)      
print(my_list)                  #[[1, 2, 15, 5, 9]

my_list.insert(10,25)      
print(my_list)                  #[1, 2, 15, 5, 9, 25]


#Example 2: Inserting a Tuple (as an Element) to the List

list1 = [{1,2},[5, 6, 7]]
list1.insert(1,(3,4))
print(list1)


# insert multiple items by squeezing it into an empty slice of a list.
my_list[2:2]=[3,4,5]
print(my_list)

my_list[:]=[3,4,5]
print(my_list)

my_list[2:]=[7,8,2] #replace the value
print(my_list)