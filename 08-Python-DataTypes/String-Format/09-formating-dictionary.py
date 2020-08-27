# Example : Formatting dictionary members using format()

student = {'name':'Sara', 'age':21}
print("Name = {s[name]} and Age= {s[age]}".format(s=student))

# There's an easier way to format dictionaries in Python using str.format(**mapping).
student = {'name':'Sara', 'age':21}
print("Name = {name} and Age= {age}".format(**student))