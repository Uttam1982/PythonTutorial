# re.escape(<regex>)

# Escapes characters in a regex.

# re.escape(<regex>) returns a copy of <regex> with each nonword character 
# (anything other than a letter, digit, or underscore) preceded by a backslash.

import re

# Output : None
print(re.match('foo^bar(baz)|qux', 'foo^bar(baz)|qux'))

# Output : <re.Match object; span=(0, 16), match='foo^bar(baz)|qux'>
print(re.match(r'foo\^bar\(baz\)\|qux', 'foo^bar(baz)|qux'))

# Output : True
print(re.escape('foo^bar(baz)|qux') == r'foo\^bar\(baz\)\|qux')


# Output : <re.Match object; span=(0, 16), match='foo^bar(baz)|qux'>
print(re.match(re.escape('foo^bar(baz)|qux'), 'foo^bar(baz)|qux'))