# More than One Constructor in Single class

# Internally, the object of the class will always call the last constructor 
# if the class has multiple constructors.

class Book:

  def __init__(self):
    print('First constructor')

  def __init__(self):
    print('Second constructor')


book1 = Book()


# In the above code, the object book1 called the second constructor 
# whereas both have the same configuration. 

# The first method is not accessible by the book1 object.

#-------------------------------------------------------------------------
class Employee:

  def __init__(self):
    print('Non-parameterized constructor')

  def __init__(self, id,name):
    print('Parameterized constructor')


#emp1 = Employee()
emp2 = Employee(10,'Alex')

# The first method is not accessible by the emp2 object.

#-------------------------------------------------------------------------

# Internally, the object of the class will always call the last constructor 
# if the class has multiple constructors.