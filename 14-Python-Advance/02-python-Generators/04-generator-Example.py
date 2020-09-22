# A simple generator for Fibonacci Numbers

def fibonacci(n):
  # initialize the first two numbers
  a, b = 0, 1

  # one by one yeild the next fibonacci numbers
  while a < n:
    yield a
    a, b = b, a+b
  
# Create a generator 
gen = fibonacci(5)

print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
# Stop Iteration
# print(next(gen))


# Uisng for loop
print("------------")
for i in fibonacci(5):
  print(i)


