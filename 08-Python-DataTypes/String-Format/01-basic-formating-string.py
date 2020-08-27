# Example 1: Basic formatting for default, positional and keyword arguments

# default arguments
print("Hello {}, your balance is {}.".format("Sara", 450.3456))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Sara", 450.3456))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Sara", blc= 450.3456))

# mixed arguments
print("Hello {}, your balance is {blc}.".format("Sara", blc= 450.3456))