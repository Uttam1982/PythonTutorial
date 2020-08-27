# The format() Method for Formatting Strings

# 1. Format strings contain curly braces {} as placeholders or replacement fields 
#    which get replaced.
# 2. We can use positional arguments or keyword arguments to specify the order.

# *************************************************************************************
# default(implicit) order
print("default(implicit) order: {}, {} and {}".format('bread','butter','jam'))

# order using positional argument
print("order using positional argument: {1}, {0} and {2}".format('bread','butter','jam'))

# order using keyword argument
print("order using keyword argument: {c}, {b} and {a}".format(a='bread',b='butter',c='jam'))

# mixed
# order using keyword argument
print("mixed: {0}, {c} and {1}".format('bread','butter',c='jam'))


#https://www.programiz.com/python-programming/methods/string/format