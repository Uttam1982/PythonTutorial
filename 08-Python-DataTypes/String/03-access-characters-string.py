# How to access characters in a string?

# 1. We can access individual characters using indexing and a range of characters using slicing
# 2. Index starts from 0.
# 3. Trying to access a character out of index range will raise an IndexError
# 4. The index must be an integer. We can't use floats or other types, this 
#    will result into TypeError.
# 5. Python allows negative indexing for its sequences.
# 6. We can access a range of items in a string by using the slicing operator :(colon).

#*****************************************************************************************

my_string= "python"

for i in range(len(my_string)):
  print("my_string[",i,"] = ",my_string[i])

for i in range(len(my_string)):
  print("my_string[",-i - 1,"] = ",my_string[-i -1])


#first character
print("my_string[0]: ",my_string[0])

#last character
print("my_string[-1]: ",my_string[-1])

#slicing 2nd to 5th character
print("my_string[1:5]: ",my_string[1:5])

#slicing 2nd to 2nd last character
print("my_string[1:-1]: ",my_string[1:-1])

# index must be in range
#print("my_string[-1]: ",my_string[7])

# index must be an integer
#print("my_string[1.5]: ",my_string[1.5])

