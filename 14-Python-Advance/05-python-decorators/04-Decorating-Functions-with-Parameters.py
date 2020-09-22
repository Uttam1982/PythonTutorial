# Decorating Functions with Parameters
#----------------------------------------------------------------------
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        print("Returning the function result")
        return func(a, b)
    print("Returning from inner")    
    return inner

#----------------------------------------------------------------------
@smart_divide
def divide(a,b):
  return a/b
print(divide)
print(divide(12,2))


# Output
# <function smart_divide.<locals>.inner at 0x7fb57ed43a70>
# Returning from inner
# I am going to divide 12 and 2
# Returning the function result
# 6.0


# This new implementation will return None if the error condition arises.
print(divide)
print(divide(12,0))


# output
# <function smart_divide.<locals>.inner at 0x7fb57ed43a70>
# I am going to divide 12 and 0
# Whoops! cannot divide
# None



#----------------------------------------------------------------------
# is equivalent to

def div(a,b):
  return a / b

div = smart_divide(div)
print(div)
print(div(3,2))

# Output :
# <function smart_divide.<locals>.inner at 0x7fea8fc43b00>
# Returning from inner
# I am going to divide 3 and 2
# Returning the function result
# 1.5
print(div)
print(div(3,0))

# <function smart_divide.<locals>.inner at 0x7fea8fc43b00>
# I am going to divide 3 and 0
# Whoops! cannot divide
# None

#----------------------------------------------------------------------

