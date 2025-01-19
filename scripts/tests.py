import os

# Get the current working directory
current_directory = os.getcwd()
print('Current Directory:', current_directory)

# Move one directory back
os.chdir('..')

# Get the updated working directory
new_directory = os.getcwd()
print('Moved to Parent Directory:', new_directory)
