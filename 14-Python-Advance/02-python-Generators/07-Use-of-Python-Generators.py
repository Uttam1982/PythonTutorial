#--------------------------------------------------------------------------------
# Use of Python Generators
#--------------------------------------------------------------------------------
# There are several reasons that make generators a powerful implementation.

# 1. Easy to Implement
# 2. Memory Efficient
# 3. Represent Infinite Stream
# 4. Pipelining Generators

#--------------------------------------------------------------------------------
# 1. Easy to Implement
#--------------------------------------------------------------------------------

# Example to implement a sequence of power of 2 using an iterator class.

class PowTwo:
  def __init__(self, max = 0):
    self.max = max
    self.i =0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.i > self.max:
      raise StopIteration
    else:
      result = 2 ** self.i
      self.i += 1
      return result


it = iter(PowTwo(5))
for item in it:
  print(item, end=" ")

print()

#---------------------------------------------------------------------------------------------
# The above program was lengthy and confusing. 
# Now, let's do the same using a generator function.

def PowTwoGen(max=0):
  n = 0
  while n <= max:
    yield 2 ** n
    n = n + 1

for item in PowTwoGen(5):
  print(item, end=" ")

print()
# Since generators keep track of details automatically, the implementation 
# was concise and much cleaner.


#---------------------------------------------------------------------------------------------
# 2. Memory Efficient
#---------------------------------------------------------------------------------------------

# A normal function to return a sequence will create the entire sequence in memory 
# before returning the result. This is an overkill, if the number of items in the 
# sequence is very large.

# Generator implementation of such sequences is memory friendly and is preferred 
# since it only produces one item at a time.


#---------------------------------------------------------------------------------------------
# 3. Represent Infinite Stream
#---------------------------------------------------------------------------------------------

# Generators are excellent mediums to represent an infinite stream of data. 
# Infinite streams cannot be stored in memory, and since generators produce 
# only one item at a time, they can represent an infinite stream of data.

def all_even():
  n = 0
  while True:
    yield n
    n = n + 2

even = all_even()
for i in range(5):
  element = next(even)
  print(element, end=" ")
print()

#---------------------------------------------------------------------------------------------
# 4. Pipelining Generators
#---------------------------------------------------------------------------------------------
# Multiple generators can be used to pipeline a series of operations.

# Suppose we have a generator that produces the numbers in the Fibonacci series. 
# And we have another generator for squaring numbers.

# we want to find out the sum of squares of numbers in the Fibonacci series, 
# we can do it in the following way by pipelining the output of generator functions together.


def fibonacci_numbers(num):
  a, b = 0, 1
  for _ in range(num):
    a, b = b, a+b
    print("fibo: ",a)
    yield a

def squares(nums):
  for n in nums:
    result = n ** 2
    print("square: ",result)
    yield result
  print("**********")

print(sum(squares(fibonacci_numbers(5))))






