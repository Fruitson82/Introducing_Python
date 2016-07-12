animal = 'fruitbat'

def print_global():
	print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

def change_and_print_global():
	global animal
	animal = 'wombat'
	print('inside change_and_print_global:', animal)

change_and_print_global()
