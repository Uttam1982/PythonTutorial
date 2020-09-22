class Addition:
  def add(self,a,b):
    return a+b

class Multiplication:
  def multiply(self,a,b):
    return a*b

class Calculation(Addition, Multiplication):
  def divide(self,a,b):
    return a/b

calc = Calculation()
print("Divide: ",calc.divide(10,2))
print("Multiply: ",calc.multiply(10,2))
print("Addition: ",calc.add(10,2))

