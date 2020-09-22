def rev_str(my_str):
  length = len(my_str)
  for i in range(length -1, -1, -1):
    yield my_str[i]
  

# For loop to reverse a string
for char in reversed('uttam'):
  print(char, end=" ")

print()