# 
# The re module supports the capability to precompile a regex in Python 
# into a regular expression object that can be repeatedly used later.

#--------------------------------------------------------------------------------------------
# re.compile(<regex>, flags=0)
#--------------------------------------------------------------------------------------------
# Compiles a regex into a regular expression object.

# re.compile(<regex>) compiles <regex> and returns the corresponding regular 
# expression object. If you include a <flags> value, then the corresponding 
# flags apply to any searches performed with the object.

#--------------------------------------------------------------------------------------------
# There are two ways to use a compiled regular expression object. You can specify 

# 1. It as the first argument to the re module functions in place of <regex>:
# re_obj = re.compile(<regex>, <flags>)
# result = re.search(re_obj, <string>)


# 2. You can also invoke a method directly from a regular expression object:
# re_obj = re.compile(<regex>, <flags>)
# result = re_obj.search(<string>)


# 3. Both of the examples above are equivalent to this:
# result = re.search(<regex>, <string>, <flags>)

#--------------------------------------------------------------------------------------------