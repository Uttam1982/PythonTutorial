#-------------------------------------------------------------------------------------------
# [] - Square brackets
#-------------------------------------------------------------------------------------------
# Square brackets specifies a set of characters you wish to match.
#-------------------------------------------------------------------------------------------

import re

pattern = '[abc]'

my_list = ['a','ac','a Hey Jude','Hey a Jude','abc de ca','bhey abc','hey abc','czar']

# match() check the pattern at the start of the test string
result = [x for x in my_list if re.match(pattern,x)] 
print(result)

# search() check the pattern anywhere within test string
result = [x for x in my_list if re.search(pattern,x)]
print(result)

#-------------------------------------------------------------------------------------------
# You can also specify a range of characters using - inside square brackets.
#-------------------------------------------------------------------------------------------
# [a-e] is the same as [a,b,c,d,e]
# [1-4] is the same as [1,2,3,4]
# [0-39] is the same as [0,1,2,3,9]

#-------------------------------------------------------------------------------------------
# You can complement (invert) the character set by using caret ^ symbol 
# at the start of a square-bracket.
#-------------------------------------------------------------------------------------------
# [^abc] means any character except a, b or c
# [^0-9] means any non-digit character

import re

pattern1 = '[1-4]'
numbers = ['12','23','34','45','123','345','543','156','51234']
result = [x for x in numbers if re.match(pattern1,x)]
print(result)


pattern2 = '[^abc]' # means any character except a, b or c
test_strings= ['aef','bdf','cvb','def','dsa','qwerty']
result = [x for x in test_strings if re.match(pattern2,x)]
print(result)

#********************************************************************************************

