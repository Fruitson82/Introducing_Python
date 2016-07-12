def edit_story(words, func):
	for word in words:
		print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word): # 첫 글자를 대문자로 만들고 느낌표 붙이기
	return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + "!")
