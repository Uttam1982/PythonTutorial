# Python Input
# Up until now, our programs were static. 
# The value of variables was defined or hard coded into the source code.
# To allow flexibility, we might want to take the input from the user. 
# In Python, we have the input() function to allow this.

age = input('Enter your age : ')
print('The value of age =',age)
print('Data type of age = ',type(age))


#Here, we can see that the entered value 10 is a string, not a number. 
# To convert this into a number we can use int() or float() functions.age = input('Enter your age : ')
age = int(input('Enter your age : '))
print('The value of age =',age)
print('Data type of age = ',type(age))


