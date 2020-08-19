# This video focuses on two built-in functions print() and input() to perform I/O task in Python.
# Some of the functions like input() and print() are widely used 
# for standard input and output operations respectively.


#Python Output Using print() function
print('This sentence is output to the screen')

a = 5
print('The value of a is', a)


# The actual syntax of the print() function is:
# **********************************************************************

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# **********************************************************************
# Here, objects is the value(s) to be printed.
# The sep separator is used between the values. It defaults into a space character.
# After all values are printed, end is printed. It defaults into a new line.
# The file is the object where the values are printed and its default value is sys.stdout (screen).

print(1,2,3,4)
print(1,2,3,4, sep='-')
print(1,2,3,4, sep='#',end='$')
print('\n')

# ************************************************************************************
# Output formatting
# ************************************************************************************
# we would like to format our output to make it look attractive. 
# This can be done by using the str.format() method.

x=4; y=5
print("The value of x = {} and y= {}".format(x,y))

#Here, the curly braces {} are used as placeholders. 
# We can specify the order in which they are printed by using numbers (tuple index).
print("The value of x = {0} and y = {1}".format('bread','butter'))
print("The value of x = {1} and y = {0}".format('bread','butter'))


# We can even use keyword arguments to format the string.
print('Hi {name}, your id is: {id}'.format(name='Sam',id=1234))


# ************************************************************************************
# We can also format strings like the old sprintf() style used in C programming language. 
# We use the % operator to accomplish this.

x = 12.3456789
print('The value of x = %3.2f' %x)
print('The value of x = %3.4f' %x)
