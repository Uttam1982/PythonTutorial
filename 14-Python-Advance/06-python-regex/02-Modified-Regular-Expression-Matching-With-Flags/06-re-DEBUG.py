# re.DEBUG
#----------------------------------------------------------------------------------------------
# Displays debugging information.

# The DEBUG flag causes the regex parser in Python to display debugging 
# information about the parsing process to the console:

#----------------------------------------------------------------------------------------------
import re

print(re.search('sam.joe', 'samxjoe', re.DEBUG))

# Output:
# LITERAL 115
# LITERAL 97
# LITERAL 109
# ANY None
# LITERAL 106
# LITERAL 111
# LITERAL 101

#  0. INFO 12 0b1 7 7 (to 13)
#       prefix_skip 3
#       prefix [0x73, 0x61, 0x6d] ('sam')
#       overlap [0, 0, 0]
# 13: LITERAL 0x73 ('s')
# 15. LITERAL 0x61 ('a')
# 17. LITERAL 0x6d ('m')
# 19. ANY
# 20. LITERAL 0x6a ('j')
# 22. LITERAL 0x6f ('o')
# 24. LITERAL 0x65 ('e')
# 26. SUCCESS
# <re.Match object; span=(0, 7), match='samxjoe'>


# When the parser displays LITERAL nnn in the debugging output, 
# it’s showing the ASCII code of a literal character in the regex. 
# In this case, the literal characters are 's', 'a', 'm' and 'j', 'o', 'e'.

#----------------------------------------------------------------------------------------------

# This is the phone number regex shown in the discussion on the VERBOSE flag earlier:

regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

print(re.search(regex,'123-4567', re.DEBUG))

# AT AT_BEGINNING
# MAX_REPEAT 0 1
#   SUBPATTERN 1 0 0
#     LITERAL 40
#     MAX_REPEAT 3 3
#       IN
#         CATEGORY CATEGORY_DIGIT
#     LITERAL 41
# MAX_REPEAT 0 MAXREPEAT
#   IN
#     CATEGORY CATEGORY_SPACE
# MAX_REPEAT 3 3
#   IN
#     CATEGORY CATEGORY_DIGIT
# IN
#   LITERAL 45
#   LITERAL 46
# MAX_REPEAT 4 4
#   IN
#     CATEGORY CATEGORY_DIGIT
# AT AT_END

#  0. INFO 4 0b0 8 MAXREPEAT (to 5)
#  5: AT BEGINNING
#  7. REPEAT 21 0 1 (to 29)
# 11.   MARK 0
# 13.   LITERAL 0x28 ('(')
# 15.   REPEAT_ONE 9 3 3 (to 25)
# 19.     IN 4 (to 24)
# 21.       CATEGORY UNI_DIGIT
# 23.       FAILURE
# 24:     SUCCESS
# 25:   LITERAL 0x29 (')')
# 27.   MARK 1
# 29: MAX_UNTIL
# 30. REPEAT_ONE 9 0 MAXREPEAT (to 40)
# 34.   IN 4 (to 39)
# 36.     CATEGORY UNI_SPACE
# 38.     FAILURE
# 39:   SUCCESS
# 40: REPEAT_ONE 9 3 3 (to 50)
# 44.   IN 4 (to 49)
# 46.     CATEGORY UNI_DIGIT
# 48.     FAILURE
# 49:   SUCCESS
# 50: IN 5 (to 56)
# 52.   RANGE 0x2d 0x2e ('-'-'.')
# 55.   FAILURE
# 56: REPEAT_ONE 9 4 4 (to 66)
# 60.   IN 4 (to 65)
# 62.     CATEGORY UNI_DIGIT
# 64.     FAILURE
# 65:   SUCCESS
# 66: AT END
# 68. SUCCESS
# <re.Match object; span=(0, 8), match='123-4567'>

#----------------------------------------------------------------------------------------------
# Output : <re.Match object; span=(0, 5), match='x222y'>
print(re.search('x[123]{2,4}y', 'x222y'))



print(re.search('x[123]{2,4}y', 'x222y', re.DEBUG))

# LITERAL 120
# MAX_REPEAT 2 4
#   IN
#     LITERAL 49
#     LITERAL 50
#     LITERAL 51
# LITERAL 121

#  0. INFO 8 0b1 4 6 (to 9)
#       prefix_skip 1
#       prefix [0x78] ('x')
#       overlap [0]
#  9: LITERAL 0x78 ('x')
# 11. REPEAT_ONE 10 2 4 (to 22)
# 15.   IN 5 (to 21)
# 17.     RANGE 0x31 0x33 ('1'-'3')
# 20.     FAILURE
# 21:   SUCCESS
# 22: LITERAL 0x79 ('y')
# 24. SUCCESS
# <re.Match object; span=(0, 5), match='x222y'>

#----------------------------------------------------------------------------------------------