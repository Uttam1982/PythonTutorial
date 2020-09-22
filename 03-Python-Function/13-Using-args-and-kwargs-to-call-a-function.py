# Using *args and **kwargs to call a function

def myFun(arg1,arg2,arg3):
  print('arg1: ',arg1)
  print('arg2: ',arg2)
  print('arg3: ',arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :

args = ('welcome','to','python')
myFun(*args)
print("-------------------------------------------------------")
kwargs = {'arg1':'welcome','arg2':'to','arg3':'hyderabad'}
myFun(*kwargs)


#Using *args and **kwargs in same line to call a function

def myFun1(*args,**kwargs):

    #output : args:  ('welcome', 'to', 'python')
    print("args: ", args)
    # output: kwargs:  {'first': 'Welcome', 'mid': 'to', 'last': 'hyderabad'}
    print("kwargs: ", kwargs)

# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun1('welcome','to','python', first ='Welcome',mid='to',last='hyderabad')
