def document_it(func):
	def new_function(*args, **kwargs):
		print('Runing function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function

