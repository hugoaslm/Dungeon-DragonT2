# Import the os module
import os

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
os.chdir('SRC')

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))