# Python List append()
# 1. The append() method adds an item to the end of the list.
# 2. The syntax of the append() method is:

      #list.append(item)

# 3. item - an item to be added at the end of the list
# 4. The item can be numbers, strings, dictionaries, another list, and so on.

# 5. The method doesn't return any value (returns None).

# Example : Adding Element to a List

my_list = ['Sam','Ben']
print("original list:",my_list)

# Alice append to my list
my_list.append('Alice')
print("appended list:",my_list) # ['Sam', 'Ben', 'Alice']

# list is append to my_list
my_list.append(['Joe','Dave'])
print("appended a list:",my_list)  # ['Sam', 'Ben', 'Alice', ['Joe', 'Dave']]

# If you need to add items of a list to another list (rather than the list itself), 
# use the extend() method.