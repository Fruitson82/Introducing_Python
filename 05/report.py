def get_description():
	"""Return random weather, just like the props"""
	from random import choice

	possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
	return choice(possibilities)