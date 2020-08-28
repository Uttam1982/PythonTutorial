# all()	Returns True if all elements of the set are true (or if the set is empty).

my_set = set()
print("all ",all(my_set))

my_set = {1,2,3}
print("all ",all(my_set))


my_set = {0,1,2,3}
print("all ",all(my_set))

my_set = {False,1,2,3}
print("all ",all(my_set))

my_set = {'0',1,2,3}
print("all ",all(my_set))

my_set = {'False',1,2,3}
print("all ",all(my_set))


# any()	Returns True if any element of the set is true. If the set is empty, returns False.

my_set = set()
print("any ",any(my_set))

my_set = {1,2,3}
print("any ",any(my_set))


my_set = {0,1,2,3}
print("any ",any(my_set))

my_set = {False,1,2,3}
print("any ",any(my_set))

my_set = {'0',1,2,3}
print("any ",any(my_set))

my_set = {'False',1,2,3}
print("any ",any(my_set))

my_set = {False}
print("any ",any(my_set))

my_set = {0}
print("any ",any(my_set))

my_set = {0,False}
print("any ",any(my_set))


# enumerate():	
# Returns an enumerate object. 
# It contains the index and value for all the items of the set as a pair.

names = {"sam","joe","ben","sara"}
enumerate_names = enumerate(names)

print(type(enumerate_names))

# converting to set
print(set(enumerate_names))

# # changing the default counter
enumerate_names = enumerate(names,10)

# converting to list
print(list(enumerate_names))


names = {"Sam","joe","ben","sara"}

for item in enumerate(names):
  print(item)


for count, item in enumerate(names):
  print(count, item)

#len()	Returns the length (the number of items) in the set.
names = {"sam","joe","ben","sara"}
print("length = ",len(names))

# max()	Returns the largest item in the set.
print("max = ",max(names))

# min()	Returns the smallest item in the set.
print("min = ",min(names))


# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).

# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set))
print(sorted(py_set, reverse=True))


#sum  Returns the sum of all elements in the set.
# sum() Parameters
# iterable - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
# start (optional) - this value is added to the sum of items of the iterable. 
#                    The default value of start is 0 (if omitted)

my_set = {12,13,14}
print("sum= ",sum(my_set))