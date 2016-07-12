def menu(wine, entree, dessert='pudding'):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))

print(menu('chardonnay', 'chicken', 'bagel'))

print("=============================")

def buggy(arg, result=[]):
	result.append(arg)
	print(result)

buggy('a')
buggy('b')

print("=============================")

def works(arg):
	result = []
	result.append(arg)
	print(result)

works('a')
works('b')

print("=============================")

def nonbuggy(arg, result=None):
	if result is None:
		result=[]
	result.append(arg)
	print(result)

nonbuggy('a')
nonbuggy('b')