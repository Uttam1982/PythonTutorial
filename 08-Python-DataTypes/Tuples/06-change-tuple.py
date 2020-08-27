# Changing a Tuple

# 1. Unlike lists, tuples are immutable.
# 2. This means that elements of a tuple cannot be changed once they have been assigned. 
#    But, if the element is itself a mutable data type like list, its nested items can be changed.
# 3. We can also assign a tuple to different values (reassignment).

my_tuple =(1,2,3,[4,5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 5

# However, item of mutable element can be changed
print(my_tuple)
print("my_tuple[3][1]: ",my_tuple[3][1])
my_tuple[3][1] = 9
print(my_tuple)
print("my_tuple[3][1]: ",my_tuple[3][1])

# Tuples can be reassigned
my_tuple = ('p','y','t','h','o','n')
print(my_tuple)