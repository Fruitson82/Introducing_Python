import os

name = 'oops.txt'

print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))
print(os.path.isabs('name'))
print(os.path.isabs(name))