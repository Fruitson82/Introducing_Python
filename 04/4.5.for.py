# for list
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']

for rabbit in rabbits:
	print(rabbit)

# for letter
word = 'cat'
for letter in word:
	print(letter)	

# for dictionary
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
			  'person': 'Col. Mustard'}
for card in accusation: # 혹은 for card in accusation.keys()
	print (card)
for value in accusation.values():
	print (value)
for item in accusation.items():
	print (item)
for card, content in accusation.items():
	print ('Card', card, 'has the contents', content)
