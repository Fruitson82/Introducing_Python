fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin2 = open('relativity', 'rt')
chunk = 100
while True:
	fragment = fin2.read(chunk)
	if not fragment:
		break
	poem += fragment

fin2.close()
print(len(poem))

poem = ''
fin3 = open('relativity', 'rt')
while True:
	line = fin3.readline()
	if not line:
		break
	poem += line
fin3.close()
print(len(poem)) 

poem = ''
fin4 = open('relativity', 'rt')
for line in fin4:
	poem += line
fin4.close()
print(len(poem))

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
	print(line, end='')