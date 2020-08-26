# filter() function:
# 
# 1. The Python built-in filter() function accepts a function and a list as an argument. 
# 2. It provides an effective way to filter out all elements of the sequence. 
# 3. It returns the new sequence in which the function evaluates to True.

#*******************************************************************************************

# Program to filter out only the even items from a list

my_list = [1,4,5,7,3,9,10,18, 14, 13]
new_list = list(filter(lambda x: (x % 2 == 0),my_list))
print(new_list)


# Program to filter out only the even items from a tuple
my_tuple = (1,4,5,7,3,9,10,18, 14, 13)
new_list = list(filter(lambda x: x % 2 == 0, my_tuple))
print(new_list)

