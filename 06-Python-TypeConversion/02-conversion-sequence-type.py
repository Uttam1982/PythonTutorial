# We can even convert one sequence to another.

#Example : to convert list to set
s = set([1,2,3])
print('s = ',s)
print('Data type: ', type(s))

# Example to convert set to tuple
t = tuple({4,5,6})
print('t = ',t)
print('Data type: ', type(t))

#Example to convert list to dictionary
d = dict([[1,20],[2,40]])
print('d = ',d)
print('Data type: ', type(d))

# Example to convert string to list
s= 'python'
lst= list(s)
print('l = ',lst)               #'p', 'y', 't', 'h', 'o', 'n']
print('Data type: ', type(lst)) # Data type:  <class 'list'>