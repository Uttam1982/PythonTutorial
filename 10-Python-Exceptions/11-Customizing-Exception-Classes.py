class SalaryNotInRangeError(Exception):
  """ Exception raise for error in the input salary

  Attribites:
    salary -- input salary that cause the error
    message -- explanation of the error
  """
  def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
    self.salary = salary
    self.message = message
    super().__init__(self.message)

  def __str__(self):
          return f'{self.salary} -> {self.message}'  


  # we have overridden the constructor of the Exception class to accept our own 
  # custom arguments salary and message. Then, the constructor of the 
  # parent Exception class is called manually with the self.message argument using super().

  # The inherited __str__ method of the Exception class is then used to display 
  # the corresponding message when SalaryNotInRangeError is raised.

  # We can also customize the __str__ method itself by overriding it.



salary = int(input("Enter the salary amount:  "))
if not 5000 < salary < 15000:
  raise SalaryNotInRangeError(salary)

print(f"The salary is {salary}")
