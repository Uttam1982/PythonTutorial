# 1. Generator expressions can be used as function arguments. 
# 2. When used in such a way, the round parentheses can be dropped.
#--------------------------------------------------------------------------

my_list = [2,3,4,5]
print(sum(x * x for x in my_list))

