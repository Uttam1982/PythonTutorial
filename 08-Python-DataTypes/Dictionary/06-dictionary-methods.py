#********************************************************************************************
# copy()	Returns a shallow copy of the dictionary.
#********************************************************************************************
my_dict = {1:'Sam',2:'Ben',3:'Joe',4:'Sara',5:'Alice'}
new_dict = my_dict.copy()

#update new_dict
new_dict[5]='Dave'
#updated value of new_dict
print(new_dict)
# no change to the my_dict
print(my_dict) 

#********************************************************************************************
# items()	Return a new object of the dictionary's items in (key, value) format.
#********************************************************************************************
for item in my_dict.items():
  print(item)

for key,value in my_dict.items():
  print(key, value)

#********************************************************************************************
# keys()	Returns a new object of the dictionary's keys.
#********************************************************************************************
print("Keys")
for key in my_dict.keys():
  print(key)

#********************************************************************************************
# values()	Returns a new object of the dictionary's values
#********************************************************************************************
print("Values")
for val in my_dict.values():
  print(val)

#********************************************************************************************
# update([other])	Updates the dictionary with the key/value pairs from other, 
# overwriting existing keys.
#********************************************************************************************

my_dict = {1:'Sam',2:'Ben'}
print("original dict:",my_dict)

new_dict = {2:'Joe'}
my_dict.update(new_dict)
print("updated dict",my_dict)

new_dict = {3:'Alice',4:'Sara'}
my_dict.update(new_dict)
print("updated dict",my_dict)

#********************************************************************************************
# update() When Tuple is Passed
#********************************************************************************************
my_dict = {'x':1}
my_dict.update(y=2,z=3)
print("updated dict",my_dict)

#********************************************************************************************
# fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v 
# (defaults to None).
#********************************************************************************************
marks = {}
marks= marks.fromkeys(['English','Math','Science'],0)
print(marks)

#********************************************************************************************
for item in marks.items():
    print(item)

#********************************************************************************************
# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

#********************************************************************************************

