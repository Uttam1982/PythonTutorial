#------------------------------------------------------------------------------------
# Object
#------------------------------------------------------------------------------------
# An object (instance) is an instantiation of a class. 

# When class is defined, only the description for the object is defined. 
# Therefore, no memory or storage is allocated.

# The example for object of parrot class can be:

#------------------------------------------------------------------------------------
class Student:

  # class attribute
  college = 'Havard University'

  # instance attribute
  def __init__(self, name,age):
    self.name = name
    self.age = age


# instantiate the Student class

student1 = Student('Sam',23)
student2 = Student('Ben',24)

# Here, student1, student 2 is an object of class Student.

#access the class attribute
print("\nAccessing class variable using object reference") 
print(f"College Name: {student1.college}")
print(f"College Name: {student2.__class__.college}")

print("\nAccessing class variable using class name") 
print(f"College Name: {Student.college}")

#access the instance attribute
print("\nAccessing instance variable") 
print(f"{student1.name} is {student1.age} years old")
print(f"{student2.name} is {student2.age} years old")

#------------------------------------------------------------------------------------

# We created a class with the name Student. Then, we define attributes.
# These attributes are defined inside the __init__ method of the class. 
# It is the initializer method that is first run as soon as the object is created.

# Then, we create instances of the Parrot class. Here, student1 and student2 are references 
# (value) to our new objects.

# We can access the class attribute using __class__.species. 
# Class attributes are the same for all instances of a class. 

# we access the instance attributes using student1.name and student1.age. 
# However, instance attributes are different for every instance of a class.