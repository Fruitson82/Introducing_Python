import os

print(os.path.exists('oops.txt'))
os.remove('oops.txt')
print(os.path.exists('oops.txt'))