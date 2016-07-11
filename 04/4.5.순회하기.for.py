rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0

while current < len(rabbits):
	print(rabbits[current])
	current += 1

print("========================")

for rabbit in rabbits:
	print(rabbit)

print("========================")

word = 'cat'
for letter in word:
	print(letter)

print("========================")

accusation = {'room'  : 'ballroom',
			  'weapon': 'lead pipe',
			  'person': 'Col.Mustard'}

for card in accusation:
	print(card)

print("========================")

for value in accusation.values():
	print (value)

print("========================")

for item in accusation.items():
	print(item)

print("========================")

for card, contents in accusation.items():
	print('Card', card, 'has the contents', contents)		