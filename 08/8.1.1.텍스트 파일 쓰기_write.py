poem = '''There was a young lady named Bright,
Whoes speed was far faster than light;
She started on day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)

fout.close()

fout2 = open('relativity2', 'wt')
print(poem, file=fout2, sep='', end='')
fout2.close()

fout3 = open('relativity3', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
	if offset > size:
		break
	fout3.write(poem[offset:offset+chunk])
	offset += chunk

try:
	fout4 = open('relativity3', 'xt')
	fout.write('stomp stomp stomp')
except FileExistsError:
	print('relativity3 already exists! That was a close one.')
