import os

#os.link('oops.txt', 'yikes.txt')

#print(os.path.isfile('yikes.txt'))

print(os.path.islink('yikes.txt'))

os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))