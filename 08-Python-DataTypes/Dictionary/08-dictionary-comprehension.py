#**********************************************************************************************
# Dictionary comprehension
#**********************************************************************************************

# Dictionary comprehension is an elegant and concise way to create a new dictionary 
# from an iterable in Python.

# Dictionary comprehension consists of an expression pair (key: value) followed by 
# a for statement inside curly braces {}.

#**********************************************************************************************

# Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#**********************************************************************************************
# This code is equivalent to
squares = {}
for x in range(6):
  squares[x] = x*x
print(squares)

#**********************************************************************************************
# A dictionary comprehension can optionally contain more for or if statements.

# An optional if statement can filter out items to form the new dictionary.


odd_squares = {x: x*x for x in range(1,11) if x%2 == 1}
print(odd_squares)

#**********************************************************************************************
# Example : How to use Dictionary Comprehension

#item price in dollar

dollar_price = {'milk':1.02,'coffe':2.5,'bread':2.5}

dollar_to_pound = 0.76

pound_price = {key : value * dollar_to_pound for (key, value) in dollar_price.items()}
print(pound_price)

#**********************************************************************************************
# Example : If Conditional Dictionary Comprehension

original_dict = {'Sam':23,'Joe':46,'Ben':34,'Sara':33,'Dave':44}

# select the person whose age are even

age_even_dict = {key : value for (key, value) in original_dict.items() if value%2 == 0}
print(age_even_dict)

#**********************************************************************************************
# Example : Multiple if Conditional Dictionary Comprehension

original_dict = {'Sam':23,'Joe':46,'Ben':34,'Sara':33,'Dave':44,'Alice':28}

# select the person whose age are even and less than 40
age_odd_less_than_forty_dict = {key:value for key,value in original_dict.items() if value%2 != 0 & value < 40}
print(age_odd_less_than_forty_dict)

#**********************************************************************************************

# Example : if-else Conditional Dictionary Comprehension
original_dict = {'Sam':23,'Joe':46,'Ben':34,'Sara':33,'Dave':44,'Alice':28}

new_dict = {key : ('old' if value > 40 else 'young') 
    for key,value in original_dict.items()}

print(new_dict)

#**********************************************************************************************
# Example 7: Nested Dictionary with Two Dictionary Comprehensions

# Whenever nested dictionary comprehension is used, 
# Python first starts from the outer loop and then goes to the inner one.

nested_dict = {k1 : { k2: k1 * k2 for k2  in range(1,6)} for k1 in range(2,5)}
print(nested_dict)


#So, the above code would be equivalent to:
n_dict = dict()
for k1 in range(2,5):
  n_dict[k1] = {k2: k1 * k2 for k2 in range(1,6)}

print(n_dict)

#It can further be unfolded:
n_dict = dict()
for k1 in range(2,5):
  n_dict[k1] = dict()
  for k2 in range(1,6):
    n_dict[k1][k2] = k1 * k2

print(n_dict)

#**********************************************************************************************