# Creating Python Dictionary

# 1. Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.

# 2. An item has a key and a corresponding value that is expressed as a pair (key: value).

# 3. While the values can be of any data type and can repeat, 

# 4. keys must be of immutable type (string, number or tuple with immutable elements) and 
# 
# 5. Keys must be unique.

#1. Create an empty dictionary
my_dict = {}
print("empty dictionary: ",my_dict)
print('type of empty dictionary: ', type(my_dict))

#2. Create dictionary with integer keys
my_dict = {1:'Sam',2:'Joe',3:'Ben'}
print("dictionary with integer keys: ",my_dict)

#3. Create dictionary with mixed  keys
my_dict = {1:'Sam','marks':[90,98,89]}
print("dictionary with mixed keys: ",my_dict)

# 4. using dict() function
my_dict = dict({1:'Sam',2:'Joe',3:'Ben'})
print("using dict() function integer keys: ",my_dict)


# from sequence having each item as a pair
my_dict = dict([('name','Sam'),('age',21),('balc',1234.567)])
print("using dict() from sequence having each item as a pair: ",my_dict)


# Formatting dictionary members using format()
print("Name = {m[name]} Age = {m[age]} and Balance = {m[balc]}".format(m=my_dict))

# Format dictionaries in Python using str.format(**mapping).
print("Name = {name}, Age = {age} and Balance = {balc}".format(**my_dict))