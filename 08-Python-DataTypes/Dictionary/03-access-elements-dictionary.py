#********************************************************************************************
# Accessing Elements from Dictionary
#********************************************************************************************
# 1. Dictionary uses keys to access values

# 2. Keys can be used either inside square brackets [] or with the get() method.

# 3. If we use the square brackets [], KeyError is raised in case a key is not found 
#    in the dictionary.

# 4. The get() method returns None if the key is not found.

#********************************************************************************************

my_dict = {'id':1,'name':'Sara','age':23}

print("my_dict['id']= ",my_dict['id'])
print("my_dict['name']= ",my_dict['name'])
print("my_dict['age']= ",my_dict['age'])


#using get() method
print("Id = ",my_dict.get('id'))
print("Name = ",my_dict.get('name'))
print("Age = ",my_dict.get('age'))


# Trying to access keys which doesn't exist throws error
# get method return None
print("Salary = ",my_dict.get('salary'))

# Throws KeyError: 'salary'
print("my_dict['salary']= ",my_dict['salary'])



