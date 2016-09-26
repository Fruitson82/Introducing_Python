import os

if (os.path.exists('poems')):
	print("!!")
else :
	os.mkdir('poems')

#os.mkdir('poems/mcintyre')
#print(os.listdir('poems'))

fout = open('poems/mcintyre/the_good_man.txt', 'wt')
print('''Cheerful and happy was his mood,
	He to the poor was kind and goo,
	And he oft' times did find them food''', file=fout)

fout.close()