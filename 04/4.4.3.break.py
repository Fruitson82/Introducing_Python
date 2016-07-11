numbers = [1, 3, 4, 5, 6]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number % 2 == 0:
		print('Found even number', number)
		break
	position += 1
else: #break not call
	print('No even number found')