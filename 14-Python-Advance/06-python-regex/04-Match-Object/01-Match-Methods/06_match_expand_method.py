# match.expand(<template>)
#--------------------------------------------------------------------------------------------
# Performs backreference substitutions from a match.

# match.expand(<template>) returns the string that results from performing 
# backreference substitution on <template> exactly as re.sub() would do:

#--------------------------------------------------------------------------------------------
import re

m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')

# Output : <re.Match object; span=(0, 15), match='foo,bar,baz,aux'>
print(m)

# Output : ('bar', 'baz')
print(m.groups())

# Output : baz
print(m.expand(r'\2'))

# Output : baz
print(m.expand(r'[\3] ---> [\1]'))


m = re.search(r'(?P<num>\d+)', 'foo123qux')

# Output : re.Match object; span=(3, 6), match='123'>
print(m)

# Output : 123
print(m.group('num'))

# Output : 123
print(m.group(1))

# Output : --- 123 ---
print(m.expand(r'--- \g<num> ---'))

#--------------------------------------------------------------------------------------------