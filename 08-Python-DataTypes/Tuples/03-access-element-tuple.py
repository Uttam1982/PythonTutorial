# Access Tuple Elements
# 1. We can use the index operator [] to access an item in a tuple, where the index starts from 0.
# 2. Trying to access an index outside of the tuple index range will raise an IndexError.
# 3. The index must be an integer, so we cannot use float or other types. 
#    This will result in TypeError.

# Accessing tuple elements using indexing
my_tuple = (12,23,34,45,56,67)

print("my_tuple[0]: ",my_tuple[0]) #12
print("my_tuple[2]: ",my_tuple[2]) #34

# IndexError: list index out of range
#print("my_tuple[6]: ",my_tuple[6]) 

# Index must be an integer
# TypeError: list indices must be integers, not float
#print("my_tuple[0]: ",my_tuple[2.0]) 

# nested tuple
n_tuple= ('python',[6,7,8],(3,4,5))
#output y
print("nested tuple n_tuple[0][1]: ", n_tuple[0][1])
#output 4
print("nested tuple n_tuple[2][1]: ", n_tuple[2][1])











