# Example 1 Passing Immutable Object (String)

def change_string(str):
  str = str + "How are you ?"
  print("Inside function str = ",str)

string1 = "Hi I am there, "
change_string(string1)
print("outside function str = ",string1)


#Example 2 Passing Mutable Object (List)

def change_list(lst):
  lst.append(50)
  lst.append(60)
  print("inside function list :",lst)

list1 = [10,20,30,40]
change_list(list1)
print("outside function list :",list1)