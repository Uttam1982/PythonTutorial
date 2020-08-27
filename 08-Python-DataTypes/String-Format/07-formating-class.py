# Example : Formatting class members using format()

#define a class
class Student:
  name = 'Sara'
  age = 21

print("Name = {s.name} and Age = {s.age}".format(s= Student()))

