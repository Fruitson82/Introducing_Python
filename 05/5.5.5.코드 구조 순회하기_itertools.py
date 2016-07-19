import itertools

## chain
for items in itertools.chain([1, 2], ['a', 'b']):
	print(items)

## accumulate
for item in itertools.accumulate([1, 2, 3, 4]):
	print(item)

def multiply(a, b):
	return a * b;

for item in itertools.accumulate([1, 2, 3, 4], multiply):
	print(item)	