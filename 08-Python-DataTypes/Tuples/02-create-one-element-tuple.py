# Creating a tuple with one element is a bit tricky.

# 1. Having one element within parentheses is not enough. 
# 2. We will need a trailing comma to indicate that it is, in fact, a tuple.

my_tuple = ("python")
print("tuple without trailing comma: ",type(my_tuple)) # <class 'str'>


#Creating a tuple having one element
my_tuple = ("python",)
print("tuple with trailing comma: ",type(my_tuple)) # <class 'tuple'>


## Parentheses is optional
my_tuple = "python",
print("Parentheses is optional: ",type(my_tuple)) # <class 'tuple'>

