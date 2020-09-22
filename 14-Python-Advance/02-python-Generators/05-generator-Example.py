def integers():
  """Infinite sequence of integers"""
  i = 1
  while True:
    yield i
    i += 1

def squares():
  for i in integers():
    yield i * i

def my_fun(n, seq):
  """Returns first n values from the given sequence"""
  seq = iter(seq)
  result = []
  # result = dict()
  try:
    for i in range(1,n+1):
      result.append(next(seq))
      # result[i] = next(seq)
  except StopIteration:
    pass
  return result

print(my_fun(5, squares()))

