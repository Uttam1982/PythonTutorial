# Python Dictionary
# - Dictionary is an unordered collection of key-value pairs.
# - It is generally used when we have a huge amount of data. 
# - Dictionaries are optimized for retrieving data. 
# - We must know the key to retrieve the value

# - In Python, dictionaries are defined within braces {} 
# - with each item being a pair in the form key:value. 
# - Key and value can be of any type.


emp = {'id':101, 'name':'Sam','age':25}
print(emp)
print(type(emp))

#We use key to retrieve the respective value
print("emp['id'] = ", emp['id'])
print("emp['name'] = ", emp['name'])
print("emp['age'] = ", emp['age'])

#But not the other way around.
print("emp[2]= ", emp[2])   #KeyError: 2


