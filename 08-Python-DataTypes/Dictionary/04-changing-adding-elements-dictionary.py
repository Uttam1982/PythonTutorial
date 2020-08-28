#********************************************************************************************
# Changing and Adding Dictionary elements
#********************************************************************************************

# 1. Dictionaries are mutable. 

# 2. We can add new items or change the value of existing items using an assignment operator.

# 3. If the key is already present, then the existing value gets updated. 

# 4. In case the key is not present, a new (key: value) pair is added to the dictionary.

#********************************************************************************************

# Changing and adding Dictionary Elements

my_dict = {'name':'Sara','age':21}
print('original dict: ',my_dict)

#update the value if the key already exist
my_dict['age'] = 25
print('updated dict: ',my_dict)

# If key is not present, a new (key: value) pair is added
my_dict['city'] = 'New York'
print('added new item to  dict: ',my_dict)

#********************************************************************************************


