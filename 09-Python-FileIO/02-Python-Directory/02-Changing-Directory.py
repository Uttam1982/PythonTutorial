# Changing Directory
# We can change the current working directory by using the chdir() method.

# The new path that we want to change into must be supplied as a string to this method. 
# We can use both the forward-slash / or the backward-slash \ to separate the path elements.

# It is safer to use an escape sequence when using the backward slash.

import os
print("Change directory")

os.chdir('/Users/uttam.patra.kumar/Documents')

print(os.getcwd)

