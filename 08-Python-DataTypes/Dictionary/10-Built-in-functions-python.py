# Dictionary Built-in Functions

# 1. all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
# 2. any()	Return True if any key of the dictionary is true. 
# If the dictionary is empty, return False.
# 3. len()	Return the length (the number of items) in the dictionary.
# 4. sorted()	Return a new sorted list of keys in the dictionary.

squares = {3:9,5:25,7:49,9:81,0:0,1:1}

print(all(squares)) # False  as one of the key value is 0
print(any(squares)) # True
print(len(squares)) # 6
print(sorted(squares))

