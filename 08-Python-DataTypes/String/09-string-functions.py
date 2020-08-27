# Common Python String Methods

# Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc
# Here is a complete list of all the built-in methods to work with strings in Python.
# https://www.programiz.com/python-programming/methods/string

#***************************************************************************************
# lower() method
#***************************************************************************************
#output 'python'
print('PYTHON'.lower())


#***************************************************************************************
# upper() method
#***************************************************************************************
#output 'PYTHON'
print('python'.upper())


#***************************************************************************************
# split() method
#***************************************************************************************
#output ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
print("This will split all words into a list".split())


#***************************************************************************************
# join() method
#***************************************************************************************
# output This will join all words into a string
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))


#***************************************************************************************
# find() method
#***************************************************************************************
# output 6
print('Happy New Year'.find('New'))



#***************************************************************************************
# replace() method
#***************************************************************************************
# output 'Python is awesome!'
print('Python is great!'.replace('great','awesome'))

#***************************************************************************************
# capitalize() method
#***************************************************************************************

print('python is Great!'.capitalize())

# Non-alphabetic First Character
print('+python is Great!'.capitalize())


#***************************************************************************************
#count() method
#***************************************************************************************
# output 2
print("Python is awesome!, isn't it".count('is'))
# count after first 'i' and before the last 'i'
print("Python is awesome!, isn't it".count('is',8,25))


#***************************************************************************************
#endswith() method
#***************************************************************************************
str = "Python is easy to learn."

# output False
print(str.endswith('to learn'))

# output True
print(str.endswith('to learn.'))

# output True
print(str.endswith('Python is easy to learn.'))

## start parameter: 7
# output True
print(str.endswith('learn.',7))

# start: 7, end: 26
print(str.endswith('learn.',7,26))

#***************************************************************************************