def menu(wine, entree, dessert):
	return{'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('beef', 'bagel', 'bordeaux'))
print(menu('bordeaux', entree='beef', dessert='bagle'))

def menu2(wine, entree, dessert='pudding'):
	return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu2('chardonnay', 'chicken', 'aa'))

def buggy(arg, result=[]):
	result.append(arg)
	print(result)
buggy('a')
buggy('b')

def works(arg): 
	result = []
	result.append(arg)
	return result

print(works('a'))
print(works('b'))

def print_args(*args):
	print('Positional argument tuple: ', args) 

print_args('a', 'b', 'c')

def print_kwargs(**kwargs):
	print('Keyword arguments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

