fin = open('bfile', 'rb')
bdata = fin.read()
fin.close()
print(len(bdata))